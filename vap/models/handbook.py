"""TODO: Foundation Pack implementation."""
from dataclasses import dataclass, field

from .chapter import Chapter


@dataclass
class Handbook:
    """
    Root semantic model of the Vietnam Adventure Handbook.
    """

    title: str = ""

    subtitle: str = ""

    version: str = ""

    author: str = ""

    chapters: list[Chapter] = field(default_factory=list)

    def add_chapter(self, chapter: Chapter) -> None:
        self.chapters.append(chapter)

    @property
    def chapter_count(self) -> int:
        return len(self.chapters)

    def __len__(self):
        return len(self.chapters)

    def __iter__(self):
        return iter(self.chapters)

    def clear(self):
        self.chapters.clear()

    def get_chapter(self, number: int):
        for chapter in self.chapters:
            if getattr(chapter, "number", None) == number:
                return chapter
        return None

    def summary(self) -> dict:
        component_count = sum(
            getattr(chapter, "component_count", 0)
            for chapter in self.chapters
        )

        return {
            "title": self.title,
            "chapters": self.chapter_count,
            "components": component_count,
        }

    def __str__(self):
        return (
            f"Handbook("
            f"title='{self.title}', "
            f"chapters={self.chapter_count})"
        )