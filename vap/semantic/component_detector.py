"""
component_detector.py

Creates semantic Component objects from the paragraphs of a chapter.

A Component represents a semantic section (Travel Tip, Quick Facts,
Editor's Note, Table, Image, etc.), not an individual paragraph.
"""

from __future__ import annotations

import re

from vap.models.component import Component
from vap.models.enums import ComponentType


class ComponentDetector:
    """
    Detect semantic components inside a chapter.
    """

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def detect(self, chapter) -> list[Component]:
        paragraphs = getattr(chapter, "paragraphs", [])

        components: list[Component] = []
        current: Component | None = None

        for index, paragraph in enumerate(paragraphs):

            text = getattr(paragraph, "text", "").strip()

            if not text:
                continue

            component_type = self._detect_type(text)

            # ----------------------------------------------------------
            # Standalone placeholders
            # ----------------------------------------------------------

            if component_type == ComponentType.IMAGE:

                component = Component(
                    component_type=ComponentType.IMAGE,
                    heading=text,
                    image_index=index,
                    style_name=getattr(paragraph, "style", ""),
                    start_index=index,
                    end_index=index,
                )

                components.append(component)
                continue

            if component_type == ComponentType.QR_CODE:

                component = Component(
                    component_type=ComponentType.QR_CODE,
                    heading=text,
                    style_name=getattr(paragraph, "style", ""),
                    start_index=index,
                    end_index=index,
                )

                components.append(component)
                continue

            # ----------------------------------------------------------
            # Table detection
            # ----------------------------------------------------------

            if component_type == ComponentType.TABLE:

                component = Component(
                    component_type=ComponentType.TABLE,
                    heading="Table",
                    table_index=index,
                    style_name=getattr(paragraph, "style", ""),
                    start_index=index,
                    end_index=index,
                )

                components.append(component)
                continue

            # ----------------------------------------------------------
            # Semantic section heading
            # ----------------------------------------------------------

            if component_type != ComponentType.PARAGRAPH:

                if current is not None:
                    components.append(current)

                current = Component(
                    component_type=component_type,
                    heading=text,
                    style_name=getattr(paragraph, "style", ""),
                    start_index=index,
                    end_index=index,
                )

                continue

            # ----------------------------------------------------------
            # Normal paragraph
            # ----------------------------------------------------------

            if current is None:

                current = Component(
                    component_type=ComponentType.PARAGRAPH,
                    heading="",
                    style_name=getattr(paragraph, "style", ""),
                    start_index=index,
                    end_index=index,
                )

            current.paragraphs.append(text)
            current.end_index = index

        if current is not None:
            components.append(current)

        return components

    # ------------------------------------------------------------------
    # Semantic Detection
    # ------------------------------------------------------------------

    def _detect_type(self, text: str) -> ComponentType:

        upper = text.upper()

        # --------------------------------------------------------------
        # Semantic headings
        # --------------------------------------------------------------

        headings = {
            "QUICK FACTS": ComponentType.QUICK_FACTS,
            "TRAVEL TIP": ComponentType.TRAVEL_TIP,
            "EDITOR'S NOTE": ComponentType.EDITORS_NOTE,
            "EDITORS NOTE": ComponentType.EDITORS_NOTE,
            "BUDGET TIP": ComponentType.BUDGET_TIP,
            "CAUTION": ComponentType.CAUTION,
            "SENIOR-FRIENDLY ADVICE": ComponentType.SENIOR_ADVICE,
            "SENIOR FRIENDLY ADVICE": ComponentType.SENIOR_ADVICE,
        }

        if upper in headings:
            return headings[upper]

        # --------------------------------------------------------------
        # QR placeholders
        # --------------------------------------------------------------

        if re.search(r"\[.*QR.*\]", upper):
            return ComponentType.QR_CODE

        # --------------------------------------------------------------
        # Image placeholders
        # --------------------------------------------------------------

        if re.search(r"\[.*IMAGE.*\]", upper):
            return ComponentType.IMAGE

        if re.search(r"\[.*HERO.*\]", upper):
            return ComponentType.IMAGE

        # --------------------------------------------------------------
        # Checklist
        # --------------------------------------------------------------

        if (
            text.startswith("☐")
            or text.startswith("☑")
            or text.startswith("✓")
            or text.startswith("✔")
            or text.startswith("- [ ]")
            or text.startswith("- [x]")
            or text.startswith("* ")
        ):
            return ComponentType.CHECKLIST

        # --------------------------------------------------------------
        # Timeline
        # --------------------------------------------------------------

        if "→" in text or "↓" in text:
            return ComponentType.TIMELINE

        # --------------------------------------------------------------
        # Table
        # --------------------------------------------------------------

        if "|" in text or "\t" in text:
            return ComponentType.TABLE

        # --------------------------------------------------------------
        # Default
        # --------------------------------------------------------------

        return ComponentType.PARAGRAPH