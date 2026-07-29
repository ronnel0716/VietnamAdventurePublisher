"""
spacing.py

Standard paragraph spacing.
"""

from dataclasses import dataclass
from docx.shared import Pt


@dataclass(frozen=True)
class Spacing:

    BEFORE_TITLE = Pt(12)
    AFTER_TITLE = Pt(12)

    BEFORE_HEADING = Pt(8)
    AFTER_HEADING = Pt(4)

    BEFORE_PARAGRAPH = Pt(0)
    AFTER_PARAGRAPH = Pt(6)