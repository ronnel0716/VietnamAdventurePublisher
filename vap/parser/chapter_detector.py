"""
chapter_detector.py

Detects the main chapters from a DocumentModel.
"""

from __future__ import annotations

import re

from vap.models.chapter import Chapter
from vap.models.document import DocumentModel


class ChapterDetector:
    """
    Detects the main handbook chapters.

    Valid markers:

        CHAPTER 1
        CHAPTER 2
        CHAPTER 3
    """

    CHAPTER_PATTERN = re.compile(
        r"^CHAPTER\s+(\d+)$",
        re.IGNORECASE,
    )

    def detect(self, document: DocumentModel) -> list[Chapter]:

        chapters: list[Chapter] = []

        current: Chapter | None = None

        for paragraph in document:

            text = paragraph.text.strip()

            match = self.CHAPTER_PATTERN.match(text)

            if not match:
                continue

            number = int(match.group(1))

            title = self._find_title(
                document,
                paragraph.index + 1,
            )

            # Close previous chapter
            if current is not None:
                current.end_index = paragraph.index - 1

            current = Chapter(
                number=number,
                title=title,
                start_index=paragraph.index,
            )

            chapters.append(current)

        if current is not None:
            current.end_index = len(document) - 1

        return chapters

    @staticmethod
    def _find_title(
        document: DocumentModel,
        start_index: int,
    ) -> str:

        for paragraph in document.paragraphs[start_index:]:

            if paragraph.is_empty():
                continue

            if paragraph.style == "Heading 1":
                return paragraph.text.strip()

        return "Untitled Chapter"