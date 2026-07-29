import re
from dataclasses import dataclass
from typing import List, Optional


@dataclass(slots=True)
class ChapterInfo:
    """
    Lightweight semantic representation of a detected chapter.

    This class intentionally remains independent of the publishing
    models so the HandbookBuilder can convert it into whatever model
    it requires.
    """

    number: int
    title: str
    start: int
    end: int


class ChapterDetector:
    """
    Detects chapters from a parsed document.

    Expected document interface

        document.paragraphs

    Each paragraph should expose

        paragraph.text
        paragraph.index
    """

    CHAPTER_PATTERN = re.compile(
        r"^\s*CHAPTER\s+(\d+)\s*$",
        re.IGNORECASE,
    )

    def detect(self, document) -> List[ChapterInfo]:
        paragraphs = document.paragraphs

        chapters: List[ChapterInfo] = []
        current: Optional[ChapterInfo] = None

        total = len(paragraphs)

        for i, paragraph in enumerate(paragraphs):
            text = paragraph.text.strip()

            match = self.CHAPTER_PATTERN.match(text)

            if not match:
                continue

            # Close previous chapter
            if current is not None:
                current.end = paragraph.index - 1

            number = int(match.group(1))

            title = self._find_title(paragraphs, i)

            current = ChapterInfo(
                number=number,
                title=title,
                start=paragraph.index,
                end=total - 1,
            )

            chapters.append(current)

        return chapters

    def _find_title(self, paragraphs, chapter_index: int) -> str:
        """
        The chapter title is assumed to be the first non-empty paragraph
        immediately following the CHAPTER heading.
        """

        for paragraph in paragraphs[chapter_index + 1:]:
            text = paragraph.text.strip()

            if text:
                return text

        return f"Chapter {chapter_index + 1}"