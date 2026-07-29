"""
callout_renderer.py
"""

from vap.models.enums import ComponentType

from .base_renderer import BaseRenderer


class CalloutRenderer(BaseRenderer):

    TITLES = {

        ComponentType.QUICK_FACTS:
            "📌 Quick Facts",

        ComponentType.TRAVEL_TIP:
            "💡 Travel Tip",

        ComponentType.EDITORS_NOTE:
            "📝 Editor's Note",

        ComponentType.BUDGET_TIP:
            "💰 Budget Tip",

        ComponentType.SENIOR_ADVICE:
            "👴 Senior-Friendly Advice",

        ComponentType.CAUTION:
            "⚠ Caution",

        ComponentType.CHECKLIST:
            "☑ Checklist",

        ComponentType.TIMELINE:
            "🕒 Timeline",
    }

    def render(
        self,
        document,
        component,
    ):

        title = self.TITLES.get(
            component.component_type,
            component.heading,
        )

        self.theme.heading(
            document,
            title,
            level=3,
        )

        if component.component_type == ComponentType.CHECKLIST:

            for item in component.paragraphs:

                if item.strip():

                    document.add_paragraph(
                        item,
                        style="List Bullet",
                    )

            self.theme.blank(document)

            return

        if component.component_type == ComponentType.TIMELINE:

            for item in component.paragraphs:

                if item.strip():

                    document.add_paragraph(
                        item,
                        style="List Number",
                    )

            self.theme.blank(document)

            return

        for paragraph in component.paragraphs:

            if paragraph.strip():

                self.theme.paragraph(
                    document,
                    paragraph,
                )

        self.theme.blank(document)