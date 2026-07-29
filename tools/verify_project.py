"""
Vietnam Adventure Publisher
Project Verification Tool

Run:
    python tools/verify_project.py
"""

from __future__ import annotations

import importlib
import platform
import sys
from pathlib import Path


# -----------------------------------------------------------------------------
# Project Root
# -----------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

# Ensure the project root is on the Python import path
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


class Verifier:

    def __init__(self):
        self.errors = 0

    # -------------------------------------------------------------------------

    def heading(self, title: str):

        print()
        print("=" * 60)
        print(title)
        print("=" * 60)

    # -------------------------------------------------------------------------

    def check(self, passed: bool, message: str):

        if passed:
            print(f"[PASS] {message}")
        else:
            print(f"[FAIL] {message}")
            self.errors += 1

    # -------------------------------------------------------------------------

    def verify_environment(self):

        self.heading("Environment")

        self.check(
            sys.version_info >= (3, 11),
            f"Python Version : {platform.python_version()}",
        )

        print(f"Executable     : {sys.executable}")
        print(f"Project Root   : {ROOT}")

    # -------------------------------------------------------------------------

    def verify_structure(self):

        self.heading("Project Structure")

        folders = [
            "vap",
            "resources",
            "tests",
            "tools",
            "output",
            "logs",
        ]

        for folder in folders:
            self.check(
                (ROOT / folder).exists(),
                folder,
            )

    # -------------------------------------------------------------------------

    def verify_imports(self):

        self.heading("Python Imports")

        modules = [
            "vap",
            "vap.app",
            "vap.document",
            "vap.models",
            "vap.parser",
        ]

        for module in modules:

            try:

                importlib.import_module(module)

                self.check(True, module)

            except Exception as ex:

                self.check(False, module)

                print(f"       {type(ex).__name__}: {ex}")

    # -------------------------------------------------------------------------

    def verify_output(self):

        self.heading("Output Folders")

        self.check(
            (ROOT / "output").exists(),
            "output/",
        )

        self.check(
            (ROOT / "logs").exists(),
            "logs/",
        )

    # -------------------------------------------------------------------------

    def summary(self):

        self.heading("Summary")

        if self.errors == 0:

            print("PROJECT STATUS : PASS")

        else:

            print(f"PROJECT STATUS : FAILED ({self.errors} issues)")

    # -------------------------------------------------------------------------

    def run(self):

        print()
        print("Vietnam Adventure Publisher")
        print("Project Verification Tool")

        self.verify_environment()
        self.verify_structure()
        self.verify_imports()
        self.verify_output()
        self.summary()


# -----------------------------------------------------------------------------

if __name__ == "__main__":

    Verifier().run()