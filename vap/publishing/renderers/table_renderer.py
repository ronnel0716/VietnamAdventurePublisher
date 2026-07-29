"""
table_renderer.py
"""

from .base_renderer import BaseRenderer


class TableRenderer(BaseRenderer):

    def render(
        self,
        document,
        component,
    ):

        self.theme.heading(
            document,
            component.heading or "Table",
            level=3,
        )

        self.theme.paragraph(
            document,
            f"[TABLE #{component.table_index}]",
        )

        self.theme.blank(document)