"""
paragraph.py

Represents a paragraph extracted from a Word document.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ParagraphModel:
    """
    Represents a paragraph independent of python-docx.
    """

    index: int
    text: str
    style: str

    def is_empty(self) -> bool:
        return not self.text.strip()

    def is_heading(self) -> bool:
        return self.style.startswith("Heading")

    def __str__(self) -> str:
        return (
            f"[{self.index:04}] "
            f"{self.style:<15} "
            f"{self.text}"
        )