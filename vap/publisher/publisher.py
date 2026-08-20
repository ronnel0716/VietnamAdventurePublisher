"""
publisher.py

Coordinates the publication pipeline.
"""

from vap.models.handbook import Handbook
from vap.parser.chapter_detector import ChapterDetector
from vap.parser.component_detector import ComponentDetector


class Publisher:

    def __init__(self):

        self.chapter_detector = ChapterDetector()
        self.component_detector = ComponentDetector()

    def publish(self, document):

        handbook = Handbook()

        handbook.title = document.title

        chapters = self.chapter_detector.detect(document)

        for chapter in chapters:

            chapter.components = self.component_detector.detect(
                document=document,
                chapter=chapter,
            )

            handbook.add_chapter(chapter)

        return handbook