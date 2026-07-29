"""
paragraph_renderer.py
"""

from .base_renderer import BaseRenderer


class ParagraphRenderer(BaseRenderer):

    def render(
        self,
        document,
        component,
    ):

        if component.heading:

            self.theme.heading(
                document,
                component.heading,
                level=2,
            )

        for paragraph in component.paragraphs:

            if paragraph.strip():

                self.theme.paragraph(
                    document,
                    paragraph,
                )

        self.theme.blank(document)