"""
component_detector.py

Creates semantic Components from chapter paragraphs.
"""

from __future__ import annotations

from vap.models.component import Component
from vap.models.enums import ComponentType


class ComponentDetector:
    """
    Creates semantic Components for a chapter.
    """

    def detect(self, document, chapter):

        components = []

        paragraphs = document.paragraphs[
            chapter.start_index : chapter.end_index + 1
        ]

        for paragraph in paragraphs:

            text = paragraph.text.strip()

            if not text:
                continue

            component = Component(
                component_type=ComponentType.PARAGRAPH,
                heading="",
                paragraphs=[text],
                style_name=paragraph.style,
                start_index=paragraph.index,
                end_index=paragraph.index,
            )

            components.append(component)

        return components