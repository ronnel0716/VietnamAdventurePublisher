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

    A chapter marker must be exactly:

        CHAPTER 1
        CHAPTER 2
        ...

    Markers such as:

        CHAPTER 4 - Block 2

    are intentionally ignored.
    """

    CHAPTER_PATTERN = re.compile(
        r"^CHAPTER\s+(\d+)$",
        re.IGNORECASE,
    )

    def detect(self, document: DocumentModel) -> list[Chapter]:
        """
        Detect all chapters within the document.
        """

        chapters: list[Chapter] = []

        current: Chapter | None = None

        for paragraph in document:

            text = paragraph.text.strip()

            match = self.CHAPTER_PATTERN.match(text)

            if match is None:
                continue

            number = int(match.group(1))

            title = self._find_title(
                document,
                paragraph.index + 1,
            )

            if current is not None:
                current.end_paragraph = paragraph.index - 1

            current = Chapter(
                number=number,
                title=title,
                start_paragraph=paragraph.index,
            )

            chapters.append(current)

        if current is not None:
            current.end_paragraph = len(document) - 1

        return chapters

    @staticmethod
    def _find_title(
        document: DocumentModel,
        start_index: int,
    ) -> str:
        """
        Returns the first Heading 1 after the chapter marker.
        """

        for paragraph in document.paragraphs[start_index:]:

            if paragraph.is_empty():
                continue

            if paragraph.style == "Heading 1":
                return paragraph.text.strip()

        return "Untitled Chapter"