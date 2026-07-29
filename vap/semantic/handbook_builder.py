"""
handbook_builder.py

Builds the semantic Handbook model from a parsed document.
"""

from vap.models.handbook import Handbook
from .chapter_detector import ChapterDetector
from .block_detector import BlockDetector
from .component_detector import ComponentDetector


class HandbookBuilder:
    """
    Builds the complete semantic handbook.
    """

    def __init__(self):
        self.chapter_detector = ChapterDetector()
        self.block_detector = BlockDetector()
        self.component_detector = ComponentDetector()

    def build(self, document):
        """
        Build and return a Handbook model.
        """

        handbook = Handbook()

        if hasattr(handbook, "title"):
            handbook.title = getattr(document, "title", "")

        chapters = self.chapter_detector.detect(document)

        for chapter in chapters:

            blocks = self.block_detector.detect(chapter)

            for block in blocks:
                components = self.component_detector.detect(block)

                if hasattr(block, "components"):
                    block.components = components

            if hasattr(chapter, "blocks"):
                chapter.blocks = blocks

        if hasattr(handbook, "chapters"):
            handbook.chapters = chapters

        return handbook