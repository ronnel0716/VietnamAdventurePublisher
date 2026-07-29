"""
component_detector.py

Builds semantic Component objects from a Block.

Current implementation:
- Each paragraph becomes a Component.
- Empty paragraphs are ignored.
- Future versions can merge paragraphs into richer semantic components
  (Travel Tip, Timeline, QR Directory, Gallery, etc.).
"""

from vap.models.component import Component


class ComponentDetector:
    """
    Detect semantic components within a Block.
    """

    def detect(self, block):
        """
        Convert block paragraphs into Component objects.
        """

        components = []

        paragraphs = getattr(block, "paragraphs", [])

        for index, paragraph in enumerate(paragraphs):

            text = getattr(paragraph, "text", "")

            if text is None:
                continue

            text = text.strip()

            if not text:
                continue

            component = Component()

            # Populate only fields that already exist
            if hasattr(component, "title"):
                component.title = text

            if hasattr(component, "text"):
                component.text = text

            if hasattr(component, "component_type"):
                component.component_type = "paragraph"

            if hasattr(component, "start_index"):
                component.start_index = index

            if hasattr(component, "end_index"):
                component.end_index = index

            components.append(component)

        return components