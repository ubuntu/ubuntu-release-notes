"""Generate Ubuntu release schedules from YAML.

Every ``docs/<version>/schedule.yaml`` file is the single source of truth for
that release's schedule. From it, this module generates:

- Markdown snippets (week-by-week tables and an optional timeline) that the
  hand-written ``schedule.md`` pages pull in with the ``{include}`` directive.
- iCalendar (``.ics``) files published alongside the HTML docs, so that people
  can subscribe to the schedule in their calendar application.

Shared milestone names and links live in ``docs/_data/milestones.yaml``.

It works as a Sphinx extension (generation happens automatically on every
build) and as a command-line tool, mainly for validating the YAML in CI::

    python3 docs/_ext/release_schedule.py --check
    python3 docs/_ext/release_schedule.py --ics-dir /tmp/calendars
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import hashlib
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

DOCS_DIR = Path(__file__).resolve().parent.parent
GENERATED_SUBDIR = "_generated"
CALENDAR_SUBDIR = "calendar"
ALL_RELEASES_ICS = "ubuntu-releases.ics"
DEFAULT_BASE_URL = "https://documentation.ubuntu.com/release-notes/"

THURSDAY = 3
# Fixed English names: strftime() would follow the locale of whoever builds.
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]  # fmt: skip
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Invisible character used by the original tables for "same week" rows;
# an empty cell would be collapsed by some renderers.
SAME_WEEK = "\u2800"
VERSION_DIR_RE = re.compile(r"^\d+\.\d+$")
MILESTONE_ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
DATE_RE = re.compile(r"(?<![\w-])(\d{4}-\d{2}-\d{2})(?![\w-])")
QUOTING_HINT = (
    "If an item starts with '[' or contains ': ', put it in double quotes, "
    'for example: 2026-08-06: "[GNOME 50](https://example.com)"'
)


class ScheduleError(Exception):
    """A schedule YAML file is invalid."""


# --------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------


class _StrictLoader(yaml.SafeLoader):
    """SafeLoader that rejects duplicate keys.

    Plain YAML silently keeps the last of two identical keys, which would make
    an event added under an already-used date disappear without a trace.
    """


def _construct_mapping(loader, node, deep=False):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise ScheduleError(
                f"line {key_node.start_mark.line + 1}: {key} appears more than once; "
                "put all items for the same date in one list"
            )
        seen.add(key)
    return loader.construct_mapping(node, deep)


_StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


def _find_invalid_date(path: Path) -> str:
    """Locate a date such as 2026-02-30 that YAML rejected without a position."""
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        for match in DATE_RE.finditer(line.split("#")[0]):
            try:
                dt.date.fromisoformat(match.group(1))
            except ValueError:
                return f"line {number}: {match.group(1)} is not a valid date"
    return "invalid date"


def _load_yaml(path: Path):
    try:
        with path.open(encoding="utf-8") as fd:
            return yaml.load(fd, Loader=_StrictLoader)  # noqa: S506 (safe subclass)
    except ScheduleError as err:
        raise ScheduleError(f"{path}: {err}") from None
    except yaml.YAMLError as err:
        raise ScheduleError(f"{path}: invalid YAML: {err}\n{QUOTING_HINT}") from None
    except ValueError:
        # Raised by PyYAML for well-formed but impossible dates.
        raise ScheduleError(f"{path}: {_find_invalid_date(path)}") from None


def plain_text(markdown: str) -> str:
    """Strip the Markdown that may appear in schedule items, for calendars."""
    text = MD_LINK_RE.sub(r"\1", markdown)
    text = re.sub(r"<(https?://[^>]+)>", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"(\*\*|__)(?=\S)(.+?)(?<=\S)\1", r"\2", text)
    text = re.sub(r"\*(?=\S)(.+?)(?<=\S)\*", r"\1", text)
    return text


@dataclass
class Item:
    """A single entry on a given date (one freeze, one milestone, ...)."""

    markdown: str
    milestone: str | None = None
    timeline: bool = False

    @property
    def text(self) -> str:
        return plain_text(self.markdown)

    @property
    def url(self) -> str | None:
        match = MD_LINK_RE.search(self.markdown)
        return match.group(2) if match else None


@dataclass
class Schedule:
    version: str
    codename: str
    start: dt.date
    release: dt.date
    timeline: bool = False
    events: dict[dt.date, list[Item]] = field(default_factory=dict)
    activities: dict[dt.date, list[Item]] = field(default_factory=dict)

    @property
    def slug(self) -> str:
        return f"ubuntu-{self.version}"

    def week(self, day: dt.date) -> int:
        """Week number, counted from the week that contains ``start``."""
        return (thursday_of(day) - self.start).days // 7 + 1

    def page_url(self, base_url: str) -> str:
        """Published URL of the schedule page (Read the Docs uses dirhtml)."""
        return f"{base_url.rstrip('/')}/{self.version}/schedule/"


def thursday_of(day: dt.date) -> dt.date:
    """The Thursday of the (Monday-to-Sunday) week containing ``day``."""
    return day + dt.timedelta(days=THURSDAY - day.weekday())


def load_milestones(path: Path) -> dict:
    data = _load_yaml(path)
    if not isinstance(data, dict):
        raise ScheduleError(f"{path}: expected milestone IDs at the top level")
    for key, value in data.items():
        where = f"{path}: milestone {key!r}"
        if not MILESTONE_ID_RE.match(str(key)):
            raise ScheduleError(f"{path}: invalid milestone ID {key!r}")
        if not isinstance(value, dict) or not isinstance(value.get("name"), str):
            raise ScheduleError(f"{where} needs a 'name' (text)")
        unknown = set(value) - {"name", "url", "timeline"}
        if unknown:
            raise ScheduleError(f"{where}: unknown key(s): {', '.join(sorted(map(str, unknown)))}")
        if not isinstance(value.get("url", ""), str):
            raise ScheduleError(f"{where}: 'url' must be text")
        if not isinstance(value.get("timeline", False), bool):
            raise ScheduleError(f"{where}: 'timeline' must be true or false")
        try:
            value["name"].format(version="0.0", n=1)
        except (KeyError, IndexError, ValueError) as err:
            raise ScheduleError(
                f"{where}: invalid placeholder in 'name' ({err}); only {{version}} and {{n}} exist"
            ) from None
    return data


def _as_date(value, what: str, path: Path) -> dt.date:
    if isinstance(value, dt.datetime):
        raise ScheduleError(f"{path}: {what} must be a date without a time, got {value}")
    if isinstance(value, dt.date):
        return value
    raise ScheduleError(
        f"{path}: {what} must be a date in YYYY-MM-DD format, got {value!r}"
    )


def _parse_items(
    section: str, raw, milestones: dict, version: str, path: Path
) -> dict[dt.date, list[Item]]:
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise ScheduleError(f"{path}: '{section}' must map dates to text")

    # Per section, so that {n} in the 'events' isn't affected by 'activities'.
    counters: dict[str, int] = {}
    result: dict[dt.date, list[Item]] = {}
    # Sort so that numbered milestones (point releases) are counted in order.
    for key in sorted(raw, key=lambda k: str(k)):
        day = _as_date(key, f"'{section}' key", path)
        values = raw[key]
        if values is None or values == []:
            raise ScheduleError(
                f"{path}: {section}: nothing is listed for {day}; "
                "add an item or remove the date"
            )
        if not isinstance(values, list):
            values = [values]
        items = []
        for value in values:
            if not isinstance(value, str) or not value.strip():
                raise ScheduleError(
                    f"{path}: {section} on {day}: expected text, got {value!r}; "
                    "put it in double quotes"
                )
            if "\n" in value.strip():
                raise ScheduleError(
                    f"{path}: {section} on {day}: items must fit on one line; "
                    "use a list for several items"
                )
            item = _parse_item(value.strip(), milestones, version, path, counters)
            if any(other.markdown == item.markdown for other in items):
                raise ScheduleError(
                    f"{path}: {section} on {day}: {value.strip()!r} is listed twice"
                )
            items.append(item)
        result[day] = items
    return result


def _parse_item(value: str, milestones: dict, version: str, path: Path, counters: dict) -> Item:
    if value in milestones:
        info = milestones[value]
        counters[value] = counters.get(value, 0) + 1
        name = info["name"].format(version=version, n=counters[value])
        url = info.get("url")
        markdown = f"[{name}]({url})" if url else name
        return Item(markdown, milestone=value, timeline=bool(info.get("timeline")))
    if MILESTONE_ID_RE.match(value):
        # Looks like an ID rather than prose: catch typos such as
        # "feature-freze", which would otherwise be published verbatim.
        close = difflib.get_close_matches(value, milestones, n=1, cutoff=0.8)
        if close:
            raise ScheduleError(
                f"{path}: unknown milestone ID {value!r}; did you mean {close[0]!r}?"
            )
    return Item(value)


def load_schedule(path: Path, milestones: dict) -> Schedule:
    data = _load_yaml(path)
    if not isinstance(data, dict):
        raise ScheduleError(f"{path}: expected a mapping at the top level")

    allowed = {"codename", "start", "release", "timeline", "events", "activities"}
    unknown = set(data) - allowed
    if unknown:
        raise ScheduleError(f"{path}: unknown key(s): {', '.join(sorted(map(str, unknown)))}")
    for required in ("codename", "start", "release"):
        if required not in data:
            raise ScheduleError(f"{path}: missing required key '{required}'")
    if not isinstance(data.get("timeline", False), bool):
        raise ScheduleError(f"{path}: 'timeline' must be true or false")

    codename = data["codename"]
    if not isinstance(codename, str) or not codename.strip():
        raise ScheduleError(f"{path}: 'codename' must be text, such as: Resolute Raccoon")
    version = path.parent.name
    start = _as_date(data["start"], "'start'", path)
    release = _as_date(data["release"], "'release'", path)
    if start.weekday() != THURSDAY:
        raise ScheduleError(f"{path}: 'start' ({start}) must be a Thursday")
    if release <= start:
        raise ScheduleError(f"{path}: 'release' must be after 'start'")

    schedule = Schedule(
        version=version,
        codename=codename.strip(),
        start=start,
        release=release,
        timeline=data.get("timeline", False),
        events=_parse_items("events", data.get("events"), milestones, version, path),
        activities=_parse_items("activities", data.get("activities"), milestones, version, path),
    )
    for section in (schedule.events, schedule.activities):
        for day in section:
            if day < start - dt.timedelta(days=3):
                raise ScheduleError(f"{path}: {day} is before the start week ({start})")
    _check_heading(schedule, path.parent / "schedule.md")
    return schedule


def _check_heading(schedule: Schedule, page: Path) -> None:
    """The codename is also in the hand-written page heading: keep them in sync."""
    if not page.exists():
        return
    for line in page.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            if schedule.codename not in line:
                raise ScheduleError(
                    f"{page}: the heading {line[2:]!r} doesn't contain the codename "
                    f"{schedule.codename!r} from schedule.yaml; update one of them"
                )
            return


def find_schedules(docs_dir: Path = DOCS_DIR) -> list[Path]:
    paths = [
        path
        for path in docs_dir.glob("*/schedule.yaml")
        if VERSION_DIR_RE.match(path.parent.name)
    ]
    return sorted(paths, key=lambda p: tuple(int(x) for x in p.parent.name.split(".")))


def load_all(docs_dir: Path = DOCS_DIR) -> list[Schedule]:
    milestones = load_milestones(docs_dir / "_data" / "milestones.yaml")
    return [load_schedule(path, milestones) for path in find_schedules(docs_dir)]


# --------------------------------------------------------------------------
# Markdown
# --------------------------------------------------------------------------


def _fmt_day(day: dt.date) -> str:
    label = f"{MONTHS[day.month - 1]} {day.day:02d}"
    if day.weekday() != THURSDAY:
        label += f" ({WEEKDAYS[day.weekday()]})"
    return label


def _row(*cells: str) -> str:
    return "| " + " | ".join(cells) + " |"


def render_table(schedule: Schedule, entries: dict[dt.date, list[Item]], heading: str) -> str:
    """Week-by-week table.

    Every Thursday from ``start`` to ``release`` gets a row. Entries on other
    weekdays get their own row, in the week they belong to. Entries after the
    release (point releases) are listed after a "..." row.
    """
    release_thursday = thursday_of(schedule.release)
    days = set()
    day = schedule.start
    while day <= release_thursday:
        days.add(day)
        day += dt.timedelta(days=7)
    days.update(entries)

    lines = [_row("Week", "Date (Thursday)", heading), "|----|----|----|"]
    month = None
    last_week = None
    for day in sorted(days):
        week = schedule.week(day)
        if last_week is not None and week > last_week + 1:
            lines.append(_row("...", "", ""))
            month = None  # repeat the month heading after the gap
        new_month = (day.year, day.month) != month
        if new_month:
            month = (day.year, day.month)
            lines.append(_row(f"**{MONTHS[day.month - 1]} {day.year}**", "", ""))
        week_cell = str(week) if (week != last_week or new_month) else SAME_WEEK
        last_week = week
        text = ", ".join(item.markdown for item in entries.get(day, []))
        lines.append(_row(week_cell, _fmt_day(day), text.replace("|", "\\|")))
    return "\n".join(lines) + "\n"


def render_timeline(schedule: Schedule) -> str:
    """Block for the sphinx-timeline extension, with the key milestones.

    Empty when the schedule doesn't enable the timeline, so that an
    ``{include}`` of the file never breaks.
    """
    if not schedule.timeline:
        return ""
    lines = [":::{timeline}", ":reversed:", ""]
    for day, items in sorted(schedule.events.items()):
        if not any(item.timeline for item in items):
            continue
        name = ", ".join(item.markdown for item in items)
        name = name.replace("\\", "\\\\").replace('"', '\\"')
        lines += [f"- start: {day.isoformat()}", f'  name: "{name}"']
    lines += ["", "---", "**{{dtrange}}**", "", "{{e.name}}", ":::"]
    return "\n".join(lines) + "\n"


def _calendar_link(label: str, filename: str) -> str:
    """Link to a calendar file; see the ``calendar-file`` role below."""
    return f"{{calendar-file}}`{label} <{filename}>`"


def render_calendar_links(schedule: Schedule) -> str:
    """Collapsed "add to calendar" dropdown (sphinx-design), web only."""
    return (
        "::::{only} html\n"
        ":::{dropdown} Add this schedule to your calendar\n"
        ":icon: calendar\n"
        "\n"
        f"{_calendar_link(f'Ubuntu {schedule.version} calendar', f'{schedule.slug}.ics')}"
        f" · {_calendar_link('All Ubuntu releases', ALL_RELEASES_ICS)}\n"
        "\n"
        "Download the file to import it once, or copy the link and add it "
        "to your calendar app as a subscription to receive updates. "
        "See {ref}`release-calendars`.\n"
        ":::\n"
        "::::\n"
    )


def render_calendar_index(schedules: list[Schedule]) -> str:
    """Table of all calendar files, for the "Release calendars" page."""
    lines = [
        _row("Calendar", "Release schedule", "Contents"),
        "|----|----|----|",
        _row(
            _calendar_link(ALL_RELEASES_ICS, ALL_RELEASES_ICS),
            "All releases below",
            "Release milestones only",
        ),
    ]
    for schedule in reversed(schedules):
        lines.append(
            _row(
                _calendar_link(f"{schedule.slug}.ics", f"{schedule.slug}.ics"),
                f"{{doc}}`{schedule.version} ({schedule.codename}) </{schedule.version}/schedule>`",
                "Release milestones and archive-wide activities",
            )
        )
    return "\n".join(lines) + "\n"


def render_markdown(schedules: list[Schedule]) -> dict[str, str]:
    """All generated snippets, by path relative to the output directory.

    The content doesn't depend on the builder, so that concurrent builds of
    the same sources (such as the sphinx-llm Markdown build) agree.
    """
    files = {}
    for schedule in schedules:
        parts = {
            "events.md": render_table(schedule, schedule.events, f"{schedule.version} events"),
            "activities.md": render_table(schedule, schedule.activities, "Planned activity"),
            "calendar.md": render_calendar_links(schedule),
            "timeline.md": render_timeline(schedule),
        }
        for name, body in parts.items():
            files[f"{schedule.version}/{name}"] = body
    files["calendars.md"] = render_calendar_index(schedules)
    return files


def _write_if_changed(path: Path, content: str) -> None:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    # Atomic, as more than one build can run on the same sources at once.
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


README = """\
The files in this directory are generated from docs/*/schedule.yaml by
docs/_ext/release_schedule.py on every docs build. Don't edit them: edit the
schedule.yaml files instead. Any change here is overwritten.
"""


def write_markdown(schedules: list[Schedule], out_dir: Path) -> None:
    # No "generated" comments in the snippets themselves: comments end up in
    # the output of some builders, such as the sphinx-llm Markdown build.
    files = render_markdown(schedules)
    _write_if_changed(out_dir / "README.txt", README)
    # Only rewrite on change: avoids needless rebuilds and
    # rebuild loops with sphinx-autobuild.
    for name, content in files.items():
        _write_if_changed(out_dir / name, content)
    # Remove leftovers, such as the snippets of a deleted schedule.yaml.
    for path in sorted(out_dir.rglob("*"), reverse=True):
        relative = path.relative_to(out_dir).as_posix()
        try:
            if path.is_file() and path.suffix == ".md" and relative not in files:
                path.unlink()
            elif path.is_dir() and not any(path.iterdir()):
                path.rmdir()
        except OSError:
            pass  # already removed or refilled by a concurrent build


# --------------------------------------------------------------------------
# iCalendar (RFC 5545)
# --------------------------------------------------------------------------


def _ics_escape(text: str) -> str:
    return (
        text.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")
    )


def _ics_fold(line: str) -> str:
    """Fold lines longer than 75 octets, as required by RFC 5545."""
    out, current = [], b""
    for char in line:
        encoded = char.encode("utf-8")
        if len(current) + len(encoded) > (75 if not out else 74):
            out.append(current.decode("utf-8"))
            current = b""
        current += encoded
    out.append(current.decode("utf-8"))
    return "\r\n ".join(out)


def _vevents(
    schedule: Schedule, calendar: str, include_activities: bool, stamp: str, base_url: str
) -> list[str]:
    sections = [("event", schedule.events)]
    if include_activities:
        sections.append(("activity", schedule.activities))
    page = schedule.page_url(base_url)

    lines = []
    for kind, entries in sections:
        for day, items in sorted(entries.items()):
            for item in items:
                summary = f"Ubuntu {schedule.version}: {item.text}"
                if kind == "activity":
                    summary = f"Ubuntu {schedule.version} archive: {item.text}"
                # Unique per calendar file: some apps refuse to import an
                # event that another subscribed calendar already contains.
                key = f"{calendar}|{schedule.version}|{kind}|{day}|{item.text}"
                uid = hashlib.sha1(key.encode()).hexdigest()[:16]
                description = (
                    f"Ubuntu {schedule.version} ({schedule.codename}) release schedule: {page}"
                )
                if item.url:
                    description += f"\nMore information: {item.url}"
                category = "Archive activity" if kind == "activity" else "Release milestone"
                lines += [
                    "BEGIN:VEVENT",
                    f"UID:{uid}-{schedule.slug}@release-notes.ubuntu.com",
                    f"DTSTAMP:{stamp}",
                    f"DTSTART;VALUE=DATE:{day.strftime('%Y%m%d')}",
                    f"DTEND;VALUE=DATE:{(day + dt.timedelta(days=1)).strftime('%Y%m%d')}",
                    f"SUMMARY:{_ics_escape(summary)}",
                    f"DESCRIPTION:{_ics_escape(description)}",
                    f"URL:{page}",
                    f"CATEGORIES:{category}",
                    "TRANSP:TRANSPARENT",
                    "END:VEVENT",
                ]
    return lines


def render_ics(
    name: str, calendar: str, schedules: list[Schedule], include_activities: bool, base_url: str
) -> str:
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Ubuntu//Release schedule//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        f"X-WR-CALNAME:{_ics_escape(name)}",
        "X-PUBLISHED-TTL:PT12H",
        "REFRESH-INTERVAL;VALUE=DURATION:PT12H",
    ]
    for schedule in schedules:
        lines += _vevents(schedule, calendar, include_activities, stamp, base_url)
    lines.append("END:VCALENDAR")
    return "".join(_ics_fold(line) + "\r\n" for line in lines)


def write_ics(schedules: list[Schedule], out_dir: Path, base_url: str) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    calendars = [
        (f"{s.slug}.ics", f"Ubuntu {s.version} ({s.codename})", [s], True) for s in schedules
    ]
    calendars.append((ALL_RELEASES_ICS, "Ubuntu releases", schedules, False))
    written = []
    for filename, name, members, include_activities in calendars:
        path = out_dir / filename
        content = render_ics(name, filename, members, include_activities, base_url)
        path.write_text(content, encoding="utf-8", newline="")
        written.append(path)
    for path in out_dir.glob("ubuntu-*.ics"):
        if path not in written:
            path.unlink()  # a deleted schedule.yaml
    return written


# --------------------------------------------------------------------------
# Sphinx integration
# --------------------------------------------------------------------------

# Builders whose output is the website itself, so the .ics files are
# published next to the pages and can be linked relatively. linkcheck is
# included so that it doesn't check calendar URLs that aren't published yet.
_SITE_BUILDERS = {"html", "dirhtml", "singlehtml"}
_RELATIVE_LINK_BUILDERS = _SITE_BUILDERS | {"linkcheck"}


def _base_url(app) -> str:
    """Absolute URL of the published docs, for links that must be absolute."""
    base = app.config.html_baseurl or ""
    return base if base.startswith(("http://", "https://")) else DEFAULT_BASE_URL


def _calendar_file_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """``{calendar-file}`label <file.ics>``: link to a generated calendar file.

    The target is resolved when each page is written (``_resolve_calendar_links``),
    relative to that page, as the files only exist in the build output.
    """
    from docutils import nodes
    from sphinx.util.nodes import split_explicit_title

    _, label, filename = split_explicit_title(text)
    node = nodes.reference(rawtext, label, refuri=filename, internal=False)
    node["calendar_file"] = filename
    return [node], []


def _resolve_calendar_links(app, doctree, docname):
    from docutils import nodes

    if app.builder.name in _RELATIVE_LINK_BUILDERS:
        # "26.04/schedule/" (dirhtml), "26.04/schedule.html" (html), "" (singlehtml)
        depth = app.builder.get_target_uri(docname).split("#")[0].count("/")
        base = "../" * depth + f"{CALENDAR_SUBDIR}/"
    else:
        # PDF, llms.txt and so on: point to the published website.
        base = f"{_base_url(app).rstrip('/')}/{CALENDAR_SUBDIR}/"
    for node in doctree.findall(nodes.reference):
        if "calendar_file" in node:
            node["refuri"] = base + node["calendar_file"]


def _on_builder_inited(app):
    from sphinx.errors import ExtensionError

    try:
        schedules = load_all(Path(app.srcdir))
    except ScheduleError as err:
        raise ExtensionError(f"Release schedule: {err}") from None
    write_markdown(schedules, Path(app.srcdir) / GENERATED_SUBDIR)


def _on_build_finished(app, exception):
    if exception or app.builder.name not in _SITE_BUILDERS:
        return
    schedules = load_all(Path(app.srcdir))
    write_ics(schedules, Path(app.outdir) / CALENDAR_SUBDIR, _base_url(app))


def setup(app):
    app.add_role("calendar-file", _calendar_file_role)
    app.connect("builder-inited", _on_builder_inited)
    app.connect("doctree-resolved", _resolve_calendar_links)
    app.connect("build-finished", _on_build_finished)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}


# --------------------------------------------------------------------------
# Command line
# --------------------------------------------------------------------------


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--check", action="store_true", help="only validate the YAML files")
    action.add_argument("--ics-dir", type=Path, help="write .ics files to this directory")
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help="published docs URL, linked from calendar events (default: %(default)s)",
    )
    args = parser.parse_args(argv)

    try:
        schedules = load_all()
    except ScheduleError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    for schedule in schedules:
        print(
            f"ok: {schedule.version} {schedule.codename}: "
            f"{sum(map(len, schedule.events.values()))} events, "
            f"{sum(map(len, schedule.activities.values()))} activities"
        )
    if args.ics_dir:
        for path in write_ics(schedules, args.ics_dir, args.base_url):
            print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
