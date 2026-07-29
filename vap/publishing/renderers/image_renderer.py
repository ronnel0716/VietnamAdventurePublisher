"""
image_renderer.py
"""

from .base_renderer import BaseRenderer


class ImageRenderer(BaseRenderer):

    def render(
        self,
        document,
        component,
    ):

        self.theme.heading(
            document,
            component.heading or "Image",
            level=3,
        )

        self.theme.paragraph(
            document,
            f"[IMAGE #{component.image_index}]",
        )

        self.theme.blank(document)