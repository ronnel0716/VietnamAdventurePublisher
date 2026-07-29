"""
component_detector.py

Creates semantic Component objects from parsed document elements.
"""

from vap.models.component import Component
from vap.models.enums import ComponentType


class ComponentDetector:
    """
    Converts document paragraphs into semantic Components.
    """

    def detect(self, chapter):
        components = []

        paragraphs = getattr(chapter, "paragraphs", [])

        for paragraph in paragraphs:

            text = getattr(paragraph, "text", "").strip()

            if not text:
                continue

            component = Component()

            if hasattr(component, "type"):
                component.type = ComponentType.PARAGRAPH

            if hasattr(component, "text"):
                component.text = text

            if hasattr(component, "style"):
                component.style = getattr(paragraph, "style", "")

            if hasattr(component, "source"):
                component.source = paragraph

            components.append(component)

        return components