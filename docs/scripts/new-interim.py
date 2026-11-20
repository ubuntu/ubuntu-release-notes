#!/usr/bin/env python3
"""Create a new interim release directory in docs/ from docs/template/interim.

Example:
    ./new-interim.py 26.10 "Stonking Stingray" --release-date 2026-10-15
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

DOCS_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = DOCS_DIR / "template" / "interim"
INTERIM_SUPPORT_MONTHS = 9
TEMPLATE_SUFFIX = ".jinja2"
PLACEHOLDER_DATE = "day month year"
PLACEHOLDER_MONTH = "month year"


def format_month(year: int, month: int) -> str:
    return date(year, month, 1).strftime("%B %Y")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("version", help="version number, e.g. 26.10")
    parser.add_argument("codename", help='release code name, e.g. "Stonking Stingray"')
    parser.add_argument(
        "--release-date",
        metavar="YYYY-MM-DD",
        help="release date; also used to compute the end of support",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="overwrite template files in an existing release directory",
    )
    args = parser.parse_args()

    if not re.fullmatch(r"\d{2}\.(04|10)", args.version):
        parser.error("version must look like YY.04 or YY.10")
    if args.release_date and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.release_date):
        parser.error("--release-date must be in YYYY-MM-DD format")
    if args.release_date:
        try:
            date.fromisoformat(args.release_date)
        except ValueError:
            parser.error("--release-date is not a valid date")
    return args


def build_context(args: argparse.Namespace) -> dict:
    release_date = PLACEHOLDER_DATE
    release_month = end_of_support = PLACEHOLDER_MONTH
    if args.release_date:
        released = date.fromisoformat(args.release_date)
        year, month = released.year, released.month
        release_date = f"{released.day} {format_month(year, month)}"
        release_month = format_month(year, month)
        total = year * 12 + (month - 1) + INTERIM_SUPPORT_MONTHS
        end_of_support = format_month(total // 12, total % 12 + 1)
    return {
        "codename": args.codename,
        "codename_slug": "-".join(args.codename.lower().split()),
        "version": args.version,
        "release_date": release_date,
        "release_month": release_month,
        "end_of_support": end_of_support,
    }


def main() -> int:
    args = parse_args()
    target = DOCS_DIR / args.version
    if target.exists() and not args.force:
        print(
            f"Error: {target} already exists. Use -f/--force to overwrite it.",
            file=sys.stderr,
        )
        return 1

    context = build_context(args)
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
    )

    target.mkdir(exist_ok=True)
    for source in sorted(TEMPLATE_DIR.rglob("*")):
        if not source.is_file():
            continue
        relative = source.relative_to(TEMPLATE_DIR)
        if source.suffix == TEMPLATE_SUFFIX:
            relative = relative.with_suffix("")
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix == TEMPLATE_SUFFIX:
            template = env.get_template(source.relative_to(TEMPLATE_DIR).as_posix())
            rendered = template.render(**context)
            destination.write_text(rendered, encoding="utf-8")
        else:
            destination.write_bytes(source.read_bytes())

    print(f"Created {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
