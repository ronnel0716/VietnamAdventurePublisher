"""
fonts.py

Central font definitions.
"""

from dataclasses import dataclass
from docx.shared import Pt


@dataclass(frozen=True)
class Fonts:

    BODY = "Calibri"
    HEADING = "Calibri Light"

    TITLE_SIZE = Pt(22)
    CHAPTER_SIZE = Pt(18)
    SECTION_SIZE = Pt(14)

    BODY_SIZE = Pt(11)
    SMALL_SIZE = Pt(9)