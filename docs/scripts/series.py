#!/usr/bin/env python3
"""Create a new Ubuntu release series or publish the series in development.

The ``new`` command creates a release directory from the interim or LTS templates
and adds it to the in-development toctree. The ``release`` command moves the
current development series to the supported releases and updates its release
notes.

Examples:
    ./series.py new 26.10 "Stonking Stingray" --release-date 2026-10-15
    ./series.py new 28.04 "Example Codename" --lts --release-date 2028-04-20
    ./series.py release
    ./series.py release --release-date 2027-04-22
"""

import argparse
import logging
import re
import sys
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

logger = logging.getLogger(Path(__file__).stem)

DOCS_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_ROOT = DOCS_DIR / "template"
INDEX_FILE = DOCS_DIR / "index.md"
INTERIM_SUPPORT_MONTHS = 9
LTS_SUPPORT_MONTHS = 5 * 12
PLACEHOLDER_CODENAME = "codename"
TEMPLATE_SUFFIX = ".jinja2"
DEV_CAPTION = "Currently in development"
LTS_CAPTION = "Supported LTS releases"
INTERIM_CAPTION = "Supported interim releases"
LTS_HEADING = "## LTS releases"
INTERIM_HEADING = "## Interim releases"
PLACEHOLDER_DATE = "day month year"
PLACEHOLDER_MONTH = "month year"

TOCTREE = re.compile(
    r"^(?P<fence>:{3,})\{toctree\}\n(?P<body>.*?)^(?P=fence)[ \t]*$",
    re.DOTALL | re.MULTILINE,
)
ENTRY = re.compile(
    r"^(?P<version>\d{2}\.(?:04|10))(?P<lts> LTS)? \((?P<codename>.+?)\) <[^>]+>$"
)
NOTICE = re.compile(
    r"^:::\{important\}\n"
    r"Ubuntu (?P<version>\S+)(?: LTS)? \(.+?\) is currently in development, "
    r"scheduled to be released on (?P<date>.+?)\.\n"
    r":::\n\n?",
    re.MULTILINE,
)
INTERIM_LIFESPAN = re.compile(
    r"^Ubuntu (?P<version>\d{2}\.\d{2}) will be supported for (?P<months>\d+) months, "
    r"from .+? until (?P<end>.+?)\.$",
    re.MULTILINE,
)


class ReleaseError(Exception):
    pass


def validate_release_date(parser: argparse.ArgumentParser, value: str | None) -> None:
    if value and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        parser.error("--release-date must be in YYYY-MM-DD format")
    if value:
        try:
            date.fromisoformat(value)
        except ValueError:
            parser.error("--release-date is not a valid date")


def format_month(year: int, month: int) -> str:
    return date(year, month, 1).strftime("%B %Y")


def previous_version(version: str, steps: int) -> str:
    """Return the release `steps` half-year cycles (04/10) before version."""
    year, month = (int(part) for part in version.split("."))
    total = year * 2 + (month == 10) - steps
    return f"{total // 2:02d}.{'10' if total % 2 else '04'}"


def find_codename(index_text: str, version: str) -> str | None:
    match = re.search(
        rf"^{re.escape(version)}(?: LTS)? \((.+?)\) <", index_text, re.MULTILINE
    )
    return match[1] if match else None


def lts_context(version: str, index_text: str) -> dict:
    old_interim = previous_version(version, 1)
    old_lts = previous_version(version, 4)
    context = {
        "old_interim_version": old_interim,
        "old_old_interim_version": previous_version(version, 2),
        "old_old_old_interim_version": previous_version(version, 3),
        "old_lts_version": old_lts,
        "old_old_lts_version": previous_version(version, 8),
    }
    for key, old_version in (("interim", old_interim), ("lts", old_lts)):
        codename = find_codename(index_text, old_version)
        if codename is None:
            logger.warning(
                f"no codename for {old_version} found in {INDEX_FILE.name}; "
                f'using the placeholder "{PLACEHOLDER_CODENAME}".'
            )
        context[f"old_{key}_codename"] = codename or PLACEHOLDER_CODENAME
    return context


def build_context(args: argparse.Namespace, index_text: str) -> dict:
    release_date = PLACEHOLDER_DATE
    release_month = end_of_support = PLACEHOLDER_MONTH
    if args.release_date:
        released = date.fromisoformat(args.release_date)
        year, month = released.year, released.month
        release_date = f"{released.day} {format_month(year, month)}"
        release_month = format_month(year, month)
        support = LTS_SUPPORT_MONTHS if args.lts else INTERIM_SUPPORT_MONTHS
        total = year * 12 + (month - 1) + support
        end_of_support = format_month(total // 12, total % 12 + 1)
    context = {
        "codename": args.codename,
        "codename_slug": "-".join(args.codename.lower().split()),
        "version": args.version,
        "release_date": release_date,
        "release_month": release_month,
        "end_of_support": end_of_support,
    }
    if args.lts:
        context.update(lts_context(args.version, index_text))
    return context


def add_to_index(text: str, entry: str) -> tuple[str, list[str]]:
    """Append entry to the in-development toctree.

    Returns the new index text and the entries that were already listed.
    """
    for match in TOCTREE.finditer(text):
        body = match["body"]
        if f":caption: {DEV_CAPTION}" not in body.splitlines():
            continue

        lines = body.splitlines()
        existing = [
            line for line in lines if line.strip() and not line.startswith(":")
        ]
        if entry in existing:
            return text, []
        while lines and not lines[-1].strip():
            lines.pop()
        if not existing:
            lines.append("")
        lines.append(entry)
        new_body = "\n".join(lines) + "\n"
        new_text = text[: match.start("body")] + new_body + text[match.end("body") :]
        return new_text, existing

    raise ValueError(f'no toctree with the caption "{DEV_CAPTION}" found in {INDEX_FILE}')


def new_series(args: argparse.Namespace) -> int:
    target = DOCS_DIR / args.version
    if target.exists() and not args.force:
        logger.error(f"{target} already exists. Use -f/--force to overwrite it.")
        return 1

    index_text = INDEX_FILE.read_text(encoding="utf-8")
    context = build_context(args, index_text)
    template_dir = TEMPLATE_ROOT / ("lts" if args.lts else "interim")
    logger.debug(f"Using templates from {template_dir}")
    logger.debug(f"Template context: {context}")
    try:
        new_index_text, listed = add_to_index(
            index_text, f"{args.version} ({args.codename}) <{args.version}/index>"
        )
    except ValueError as error:
        logger.error(f"{error}")
        return 1
    env = Environment(
        loader=FileSystemLoader([template_dir, TEMPLATE_ROOT]),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
    )

    target.mkdir(exist_ok=True)
    for source in sorted(template_dir.rglob("*")):
        if not source.is_file():
            continue
        relative = source.relative_to(template_dir)
        if source.suffix == TEMPLATE_SUFFIX:
            relative = relative.with_suffix("")
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Writing {destination}")
        if source.suffix == TEMPLATE_SUFFIX:
            template = env.get_template(source.relative_to(template_dir).as_posix())
            rendered = template.render(**context)
            destination.write_text(rendered, encoding="utf-8")
        else:
            destination.write_bytes(source.read_bytes())

    if listed:
        logger.warning(
            f'{INDEX_FILE.name} already lists a release under "{DEV_CAPTION}": '
            f'{", ".join(listed)}'
        )
    if new_index_text != index_text:
        INDEX_FILE.write_text(new_index_text, encoding="utf-8")
        logger.debug(f"Added the release to {INDEX_FILE}")

    print(f"Created {target}")
    return 0


def find_toctree(text: str, caption: str) -> re.Match:
    for match in TOCTREE.finditer(text):
        if f":caption: {caption}" in match["body"].splitlines():
            return match
    raise ReleaseError(f'no toctree with the caption "{caption}" found in {INDEX_FILE}')


def find_dev_series(text: str) -> tuple[str, str, bool, str]:
    """Return the version, codename, LTS flag, and toctree line of the dev series."""
    body = find_toctree(text, DEV_CAPTION)["body"]
    entries = [line for line in body.splitlines() if line.strip() and line[0] != ":"]
    if len(entries) != 1:
        raise ReleaseError(
            f'expected exactly one series under "{DEV_CAPTION}", found {len(entries)}'
        )
    match = ENTRY.match(entries[0].strip())
    if not match:
        raise ReleaseError(f"cannot parse the toctree entry: {entries[0]}")
    return match["version"], match["codename"], bool(match["lts"]), entries[0]


def move_toctree_entry(text: str, entry: str, target_caption: str) -> str:
    """Remove entry from the in-development toctree and put it first in the target."""
    dev = find_toctree(text, DEV_CAPTION)
    body = "".join(
        line + "\n" for line in dev["body"].splitlines() if line.rstrip() != entry.rstrip()
    )
    text = text[: dev.start("body")] + body + text[dev.end("body") :]

    target = find_toctree(text, target_caption)
    lines = target["body"].splitlines()
    existing = [i for i, line in enumerate(lines) if line.strip() and line[0] != ":"]
    if existing:
        lines.insert(existing[0], entry)
    else:
        lines += ["", entry]
    new_body = "\n".join(lines) + "\n"
    return text[: target.start("body")] + new_body + text[target.end("body") :]


def add_to_section(text: str, heading: str, block: str, marker: str) -> str:
    """Insert block right after heading, unless marker is already in that section."""
    match = re.search(rf"^{re.escape(heading)}\n\n", text, re.MULTILINE)
    if not match:
        raise ReleaseError(f'no "{heading}" section found in {INDEX_FILE}')
    section_end = re.compile(r"^## ", re.MULTILINE).search(text, match.end())
    section = text[match.end() : section_end.start() if section_end else len(text)]
    if marker in section:
        logger.warning(f"{INDEX_FILE.name} already lists {marker}")
        return text
    return text[: match.end()] + block + text[match.end() :]


def format_date(value: date) -> str:
    return f"{value.day} {value.strftime('%B %Y')}"


def update_release_page(
    path: Path, version: str, is_lts: bool, release_date: str | None
) -> None:
    text = path.read_text(encoding="utf-8")
    notice = NOTICE.search(text)
    if not notice:
        raise ReleaseError(f"no in-development notice found in {path}")
    planned = notice["date"]
    released = (
        format_date(date.fromisoformat(release_date)) if release_date else planned
    )
    text = text[: notice.start()] + text[notice.end() :]

    if is_lts:
        if release_date:
            text, count = re.subn(
                rf"^(:::\{{rubric\}}) {re.escape(planned)}$",
                rf"\1 {released}",
                text,
                flags=re.MULTILINE,
            )
            if not count:
                logger.warning(f"no rubric with {planned} found in {path.name}")
    else:
        lifespan = INTERIM_LIFESPAN.search(text)
        if not lifespan:
            raise ReleaseError(f"no support lifespan sentence found in {path}")
        replacement = (
            f"Ubuntu {version} was released on {released}. "
            f"It will be supported for {lifespan['months']} months, "
            f"until {lifespan['end']}."
        )
        text = text[: lifespan.start()] + replacement + text[lifespan.end() :]

    path.write_text(text, encoding="utf-8")
    logger.debug(f"Updated {path}")


def release_series(args: argparse.Namespace) -> int:
    index_text = INDEX_FILE.read_text(encoding="utf-8")
    try:
        version, codename, is_lts, entry = find_dev_series(index_text)
        logger.info(
            f"Releasing Ubuntu {version}{' LTS' if is_lts else ''} ({codename})"
        )
        page = DOCS_DIR / version / "index.md"
        if not page.is_file():
            raise ReleaseError(f"{page} does not exist")

        label = f"{version}{' LTS' if is_lts else ''}"
        if is_lts:
            ref = f"ubuntu-{version}-lts-release-notes"
            schedule = f"{'-'.join(codename.lower().split())}-schedule"
            block = (
                f"### {label} ({codename})\n\n"
                f"* {{ref}}`{ref}`\n"
                f"* {{ref}}`{schedule}`\n\n"
            )
            heading, marker, caption = LTS_HEADING, f"({codename})", LTS_CAPTION
        else:
            ref = f"ubuntu-{version}-release-notes"
            block = f"* {{ref}}`{ref}`\n"
            heading, marker, caption = INTERIM_HEADING, f"`{ref}`", INTERIM_CAPTION

        new_index = move_toctree_entry(index_text, entry, caption)
        new_index = add_to_section(new_index, heading, block, marker)
        update_release_page(page, version, is_lts, args.release_date)
    except ReleaseError as error:
        logger.error(f"{error}")
        return 1

    INDEX_FILE.write_text(new_index, encoding="utf-8")
    print(f"Released {label} ({codename})")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a new Ubuntu release series or publish the current one.",
        epilog=(
            "examples:\n"
            '  ./series.py new 26.10 "Stonking Stingray" --release-date 2026-10-15\n'
            "  ./series.py release --release-date 2027-04-22"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_parser = subparsers.add_parser(
        "new",
        help="create a release directory from the interim or LTS template",
        description="Create a new release directory from the interim or LTS template.",
    )
    new_parser.add_argument("version", help="version number, e.g. 26.10")
    new_parser.add_argument(
        "codename", help='release code name, e.g. "Stonking Stingray"'
    )
    new_parser.add_argument(
        "--release-date",
        metavar="YYYY-MM-DD",
        help="release date; also used to compute the end of support",
    )
    new_parser.add_argument(
        "-l",
        "--lts",
        action="store_true",
        help="use the LTS templates instead of the interim ones",
    )
    new_parser.add_argument(
        "-v", "--verbose", action="store_true", help="print debug messages"
    )
    new_parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="overwrite template files in an existing release directory",
    )
    new_parser.set_defaults(handler=new_series)

    release_parser = subparsers.add_parser(
        "release",
        help="publish the series currently in development as supported",
        description="Publish the series currently in development as supported.",
    )
    release_parser.add_argument(
        "--release-date",
        metavar="YYYY-MM-DD",
        help="actual release date; by default, the date from the release notes",
    )
    release_parser.add_argument(
        "-v", "--verbose", action="store_true", help="print debug messages"
    )
    release_parser.set_defaults(handler=release_series)

    args = parser.parse_args()
    logging.basicConfig(
        format="%(levelname)s: %(message)s",
        level=logging.DEBUG if args.verbose else logging.INFO,
    )
    if args.command == "new":
        if not re.fullmatch(r"\d{2}\.(04|10)", args.version):
            new_parser.error("version must look like YY.04 or YY.10")
        validate_release_date(new_parser, args.release_date)

        year = int(args.version[:2])
        is_lts_version = args.version.endswith(".04") and year % 2 == 0
        if is_lts_version and not args.lts:
            logger.warning(
                f"{args.version} is an LTS release, but --lts was not set. "
                "Proceeding with the interim templates. Re-run with --lts --force "
                "to overwrite the generated release notes."
            )
        elif args.lts and not is_lts_version:
            logger.warning(
                f"{args.version} is not an LTS version "
                "(LTS releases are YY.04 in even years). "
                "Proceeding with the LTS templates."
            )
    else:
        validate_release_date(release_parser, args.release_date)
    return args


def main() -> int:
    args = parse_args()
    return args.handler(args)


if __name__ == "__main__":
    sys.exit(main())
