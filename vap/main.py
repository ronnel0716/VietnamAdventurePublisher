"""
Vietnam Adventure Publisher

Command line entry point.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from vap.app.application import Application


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vap",
        description="Vietnam Adventure Publisher",
    )

    parser.add_argument(
        "source",
        help="Source DOCX handbook",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="Vietnam Adventure Handbook - Published.docx",
        help="Output DOCX filename",
    )

    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Generate PDF instead of DOCX",
    )

    return parser


def main() -> int:

    parser = build_parser()
    args = parser.parse_args()

    source = Path(args.source)

    if not source.exists():
        print(f"ERROR: Source file not found:\n{source}")
        return 1

    app = Application()

    try:

        if args.pdf:
            app.publish_pdf(source, args.output)
        else:
            app.publish_word(source, args.output)

        print()
        print("===================================")
        print(" Vietnam Adventure Publisher")
        print("===================================")
        print(f"Source : {source}")
        print(f"Output : {args.output}")
        print("Status : SUCCESS")
        print()

        return 0

    except Exception as ex:

        print()
        print("===================================")
        print(" Vietnam Adventure Publisher")
        print("===================================")
        print(f"Status : FAILED")
        print(ex)

        return 2


if __name__ == "__main__":
    sys.exit(main())