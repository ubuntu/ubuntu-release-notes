#!/usr/bin/env python3
"""Create a new release directory in docs/ from docs/template/{interim,lts}.

Examples:
    ./new-version.py 26.10 "Stonking Stingray" --release-date 2026-10-15
    ./new-version.py 28.04 "Example Codename" --lts --release-date 2028-04-20
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
INTERIM_SUPPORT_MONTHS = 9
LTS_SUPPORT_MONTHS = 5 * 12
PLACEHOLDER_CODENAME = "codename"
TEMPLATE_SUFFIX = ".jinja2"
INDEX_FILE = DOCS_DIR / "index.md"
DEV_CAPTION = "Currently in development"
PLACEHOLDER_DATE = "day month year"
PLACEHOLDER_MONTH = "month year"


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a new release directory from the interim or LTS template."
    )
    parser.add_argument("version", help="version number, e.g. 26.10")
    parser.add_argument("codename", help='release code name, e.g. "Stonking Stingray"')
    parser.add_argument(
        "--release-date",
        metavar="YYYY-MM-DD",
        help="release date; also used to compute the end of support",
    )
    parser.add_argument(
        "-l",
        "--lts",
        action="store_true",
        help="use the LTS templates instead of the interim ones",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="print debug messages",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="overwrite template files in an existing release directory",
    )
    args = parser.parse_args()
    logging.basicConfig(
        format="%(levelname)s: %(message)s",
        level=logging.DEBUG if args.verbose else logging.INFO,
    )

    if not re.fullmatch(r"\d{2}\.(04|10)", args.version):
        parser.error("version must look like YY.04 or YY.10")
    if args.release_date and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.release_date):
        parser.error("--release-date must be in YYYY-MM-DD format")
    if args.release_date:
        try:
            date.fromisoformat(args.release_date)
        except ValueError:
            parser.error("--release-date is not a valid date")

    year = int(args.version[:2])
    is_lts_version = args.version.endswith(".04") and year % 2 == 0
    if is_lts_version and not args.lts:
        logger.warning(
            "%s is an LTS release, but --lts was not set. "
            "Proceeding with the interim templates. Re-run with --lts --force "
            "to overwrite the generated release notes.",
            args.version,
        )
    elif args.lts and not is_lts_version:
        logger.warning(
            "%s is not an LTS version (LTS releases are YY.04 in even years). "
            "Proceeding with the LTS templates.",
            args.version,
        )
    return args


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
                'no codename for %s found in %s; using the placeholder "%s".',
                old_version,
                INDEX_FILE.name,
                PLACEHOLDER_CODENAME,
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
    pattern = re.compile(
        r"^(?P<fence>:{3,})\{toctree\}\n(?P<body>.*?)^(?P=fence)[ \t]*$",
        re.DOTALL | re.MULTILINE,
    )
    for match in pattern.finditer(text):
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


def main() -> int:
    args = parse_args()
    target = DOCS_DIR / args.version
    if target.exists() and not args.force:
        logger.error("%s already exists. Use -f/--force to overwrite it.", target)
        return 1

    index_text = INDEX_FILE.read_text(encoding="utf-8")
    context = build_context(args, index_text)
    template_dir = TEMPLATE_ROOT / ("lts" if args.lts else "interim")
    logger.debug("Using templates from %s", template_dir)
    logger.debug("Template context: %s", context)
    try:
        new_index_text, listed = add_to_index(
            index_text, f"{args.version} ({args.codename}) <{args.version}/index>"
        )
    except ValueError as error:
        logger.error("%s", error)
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
        logger.debug("Writing %s", destination)
        if source.suffix == TEMPLATE_SUFFIX:
            template = env.get_template(source.relative_to(template_dir).as_posix())
            rendered = template.render(**context)
            destination.write_text(rendered, encoding="utf-8")
        else:
            destination.write_bytes(source.read_bytes())

    if listed:
        logger.warning(
            '%s already lists a release under "%s": %s',
            INDEX_FILE.name,
            DEV_CAPTION,
            ", ".join(listed),
        )
    if new_index_text != index_text:
        INDEX_FILE.write_text(new_index_text, encoding="utf-8")
        logger.debug("Added the release to %s", INDEX_FILE)

    print(f"Created {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
