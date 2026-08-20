"""
styles.py

Applies common formatting to python-docx objects.
"""

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

from .fonts import Fonts
from .spacing import Spacing


class Styles:

    @staticmethod
    def heading(paragraph):

        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

        fmt = paragraph.paragraph_format
        fmt.space_before = Spacing.BEFORE_HEADING
        fmt.space_after = Spacing.AFTER_HEADING

        for run in paragraph.runs:
            run.font.name = Fonts.HEADING
            run.font.size = Fonts.SECTION_SIZE
            run.bold = True

    @staticmethod
    def body(paragraph):

        fmt = paragraph.paragraph_format
        fmt.space_before = Spacing.BEFORE_PARAGRAPH
        fmt.space_after = Spacing.AFTER_PARAGRAPH

        for run in paragraph.runs:
            run.font.name = Fonts.BODY
            run.font.size = Fonts.BODY_SIZE