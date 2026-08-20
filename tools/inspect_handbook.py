"""
Handbook Inspection Tool

Usage:
    python tools/inspect_handbook.py handbook/source/your.docx
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from vap.app.application import Application


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "source",
        help="Source DOCX handbook"
    )

    args = parser.parse_args()

    source = Path(args.source)

    if not source.exists():
        print(f"Source not found:\n{source}")
        return

    print("=" * 60)
    print("Vietnam Adventure Publisher")
    print("Handbook Inspection")
    print("=" * 60)

    app = Application()

    handbook = app.build_handbook(source)

    print()
    print("Title")
    print("-----")
    print(getattr(handbook, "title", "<No Title>"))

    chapters = getattr(handbook, "chapters", [])

    print()
    print(f"Chapters : {len(chapters)}")

    total_components = 0

    component_types = {}

    for chapter in chapters:

        components = getattr(chapter, "components", [])

        total_components += len(components)

        for component in components:

            name = component.__class__.__name__

            component_types[name] = (
                component_types.get(name, 0) + 1
            )

    print(f"Components : {total_components}")

    print()
    print("Component Breakdown")
    print("-------------------")

    if component_types:

        for name in sorted(component_types):
            print(f"{name:<25} {component_types[name]}")

    else:

        print("No components detected.")

    print()
    print("READY FOR VALIDATION")


if __name__ == "__main__":
    main()