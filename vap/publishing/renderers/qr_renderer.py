"""
qr_renderer.py
"""

from .base_renderer import BaseRenderer


class QRRenderer(BaseRenderer):

    def render(
        self,
        document,
        component,
    ):

        self.theme.heading(
            document,
            component.heading or "QR Code",
            level=3,
        )

        self.theme.paragraph(
            document,
            "[QR CODE PLACEHOLDER]",
        )

        self.theme.blank(document)