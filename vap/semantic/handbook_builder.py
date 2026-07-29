"""
handbook_builder.py

Builds the semantic Handbook model from a parsed document.
"""

from vap.models.handbook import Handbook
from vap.models.chapter import Chapter

from .chapter_detector import ChapterDetector
from .component_detector import ComponentDetector


class HandbookBuilder:
    """
    Builds a semantic Handbook from a parsed document.
    """

    def __init__(self):
        self.chapter_detector = ChapterDetector()
        self.component_detector = ComponentDetector()

    def build(self, document) -> Handbook:
        handbook = Handbook()

        if hasattr(handbook, "title"):
            handbook.title = getattr(document, "title", "")

        chapter_infos = self.chapter_detector.detect(document)

        paragraphs = getattr(document, "paragraphs", [])

        for info in chapter_infos:

            chapter = Chapter(
                number=info.number,
                title=info.title,
                start_index=info.start,
                end_index=info.end,
            )

            # Attach document paragraphs belonging to this chapter.
            chapter.paragraphs = paragraphs[
                info.start: info.end + 1
            ]

            # Detect semantic components.
            chapter.components = self.component_detector.detect(
                chapter
            )

            handbook.add_chapter(chapter)

        return handbook