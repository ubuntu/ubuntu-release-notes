#!/usr/bin/env python3
"""Publish the series that is currently in development as fully supported.

The series is the one listed under "Currently in development" in docs/index.md.
The script:

* moves the series to the supported LTS or interim toctree in docs/index.md,
* lists the series in the LTS or interim release sections in docs/index.md,
* removes the "currently in development" notice from the release notes,
* for interim releases, states the release date in the support lifespan.

Examples:
    ./release-series.py
    ./release-series.py --release-date 2027-04-22
"""

import argparse
import logging
import re
import sys
from datetime import date
from pathlib import Path

logger = logging.getLogger(Path(__file__).stem)

DOCS_DIR = Path(__file__).resolve().parent.parent
INDEX_FILE = DOCS_DIR / "index.md"
DEV_CAPTION = "Currently in development"
LTS_CAPTION = "Supported LTS releases"
INTERIM_CAPTION = "Supported interim releases"
LTS_HEADING = "## LTS releases"
INTERIM_HEADING = "## Interim releases"

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Publish the series currently in development as supported."
    )
    parser.add_argument(
        "--release-date",
        metavar="YYYY-MM-DD",
        help="actual release date; by default, the date from the release notes",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="print debug messages"
    )
    args = parser.parse_args()
    logging.basicConfig(
        format="%(levelname)s: %(message)s",
        level=logging.DEBUG if args.verbose else logging.INFO,
    )
    if args.release_date:
        try:
            date.fromisoformat(args.release_date)
        except ValueError:
            parser.error("--release-date must be a valid date in YYYY-MM-DD format")
    return args


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
        logger.warning("%s already lists %s", INDEX_FILE.name, marker)
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
                logger.warning("no rubric with %s found in %s", planned, path.name)
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
    logger.debug("Updated %s", path)


def main() -> int:
    args = parse_args()
    index_text = INDEX_FILE.read_text(encoding="utf-8")
    try:
        version, codename, is_lts, entry = find_dev_series(index_text)
        logger.info(
            "Releasing Ubuntu %s%s (%s)", version, " LTS" if is_lts else "", codename
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
        logger.error("%s", error)
        return 1

    INDEX_FILE.write_text(new_index, encoding="utf-8")
    print(f"Released {label} ({codename})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
