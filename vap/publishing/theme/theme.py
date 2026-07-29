"""
theme.py

High-level theme used by renderers.
"""

from .styles import Styles


class Theme:

    def heading(self, document, text, level=2):

        paragraph = document.add_heading(text, level)

        Styles.heading(paragraph)

        return paragraph

    def paragraph(self, document, text):

        paragraph = document.add_paragraph(text)

        Styles.body(paragraph)

        return paragraph

    def blank(self, document):

        document.add_paragraph("")