"""
Project Statistics Tool

Usage:
    python tools/stats.py
"""

from __future__ import annotations

import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


class Stats:

    def __init__(self):

        self.python_files = []

        self.total_lines = 0
        self.blank_lines = 0
        self.comment_lines = 0

        self.classes = 0
        self.functions = 0
        self.methods = 0

    # -------------------------------------------------------------

    def find_python_files(self):

        self.python_files = sorted(ROOT.rglob("*.py"))

    # -------------------------------------------------------------

    def analyze_file(self, file: Path):

        text = file.read_text(encoding="utf-8", errors="ignore")

        lines = text.splitlines()

        self.total_lines += len(lines)

        for line in lines:

            stripped = line.strip()

            if not stripped:
                self.blank_lines += 1

            elif stripped.startswith("#"):
                self.comment_lines += 1

        tree = ast.parse(text)

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):
                self.classes += 1

            elif isinstance(node, ast.FunctionDef):

                if isinstance(getattr(node, "parent", None), ast.ClassDef):
                    self.methods += 1
                else:
                    self.functions += 1

    # -------------------------------------------------------------

    def attach_parents(self, tree):

        for parent in ast.walk(tree):

            for child in ast.iter_child_nodes(parent):
                child.parent = parent

    # -------------------------------------------------------------

    def analyze(self):

        for file in self.python_files:

            text = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            tree = ast.parse(text)

            self.attach_parents(tree)

            lines = text.splitlines()

            self.total_lines += len(lines)

            for line in lines:

                stripped = line.strip()

                if not stripped:
                    self.blank_lines += 1

                elif stripped.startswith("#"):
                    self.comment_lines += 1

            for node in ast.walk(tree):

                if isinstance(node, ast.ClassDef):
                    self.classes += 1

                elif isinstance(node, ast.FunctionDef):

                    if isinstance(
                        getattr(node, "parent", None),
                        ast.ClassDef,
                    ):
                        self.methods += 1
                    else:
                        self.functions += 1

    # -------------------------------------------------------------

    def largest_files(self):

        items = []

        for file in self.python_files:

            count = len(
                file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).splitlines()
            )

            items.append((count, file))

        return sorted(
            items,
            reverse=True,
        )

    # -------------------------------------------------------------

    def packages(self):

        return len(
            list(ROOT.rglob("__init__.py"))
        )

    # -------------------------------------------------------------

    def report(self):

        print()
        print("=" * 60)
        print("Vietnam Adventure Publisher")
        print("Project Statistics")
        print("=" * 60)

        print()

        print("Project Root")
        print("------------")
        print(ROOT)

        print()

        print(f"Packages       : {self.packages()}")
        print(f"Python Files   : {len(self.python_files)}")
        print(f"Classes        : {self.classes}")
        print(f"Functions      : {self.functions}")
        print(f"Methods        : {self.methods}")

        print()

        print(f"Lines          : {self.total_lines}")
        print(f"Blank          : {self.blank_lines}")
        print(f"Comments       : {self.comment_lines}")

        print()

        largest = self.largest_files()

        if largest:

            lines, file = largest[0]

            print("Largest File")
            print("------------")
            print(file.relative_to(ROOT))
            print(f"{lines:,} lines")

        print()

        print("=" * 60)
        print("Top 10 Largest Files")
        print("=" * 60)

        for lines, file in largest[:10]:

            print(
                f"{lines:>6}  {file.relative_to(ROOT)}"
            )

    # -------------------------------------------------------------

    def run(self):

        self.find_python_files()
        self.analyze()
        self.report()


if __name__ == "__main__":

    Stats().run()