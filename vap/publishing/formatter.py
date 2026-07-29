"""
formatter.py

Dispatches semantic components to the correct renderer.
"""

from __future__ import annotations

from vap.models.enums import ComponentType

from .renderers import (
    ParagraphRenderer,
    CalloutRenderer,
)
from .renderers.table_renderer import TableRenderer
from .renderers.image_renderer import ImageRenderer
from .renderers.qr_renderer import QRRenderer


class Formatter:

    def __init__(self):

        callout = CalloutRenderer()

        self.renderers = {

            ComponentType.PARAGRAPH:
                ParagraphRenderer(),

            ComponentType.QUICK_FACTS:
                callout,

            ComponentType.TRAVEL_TIP:
                callout,

            ComponentType.EDITORS_NOTE:
                callout,

            ComponentType.BUDGET_TIP:
                callout,

            ComponentType.SENIOR_ADVICE:
                callout,

            ComponentType.CAUTION:
                callout,

            ComponentType.CHECKLIST:
                callout,

            ComponentType.TIMELINE:
                callout,

            ComponentType.TABLE:
                TableRenderer(),

            ComponentType.IMAGE:
                ImageRenderer(),

            ComponentType.QR_CODE:
                QRRenderer(),
        }

    def render(
        self,
        document,
        component,
    ):

        renderer = self.renderers.get(
            component.component_type
        )

        if renderer is None:

            renderer = self.renderers[
                ComponentType.PARAGRAPH
            ]

        renderer.render(
            document,
            component,
        )