"""
publisher.py

Coordinates the publication pipeline.

Pipeline

Document
    ↓
Chapter Detection
    ↓
Component Detection
    ↓
Handbook
"""

from vap.parser.chapter_detector import ChapterDetector
from vap.parser.component_detector import ComponentDetector
from vap.models.handbook import Handbook


class Publisher:

    def __init__(self):

        self.chapter_detector = ChapterDetector()
        self.component_detector = ComponentDetector()

    def publish(self, document):

        handbook = Handbook()

        if hasattr(handbook, "title"):
            handbook.title = getattr(document, "title", "")

        chapters = self.chapter_detector.detect(document)

        for chapter in chapters:

            components = self.component_detector.detect(chapter)

            if hasattr(chapter, "components"):
                chapter.components = components

            if hasattr(handbook, "add_chapter"):
                handbook.add_chapter(chapter)
            elif hasattr(handbook, "chapters"):
                handbook.chapters.append(chapter)

        return handbook