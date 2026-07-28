"""
document.py

Represents a document independent of python-docx.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from vap.models.paragraph import ParagraphModel


@dataclass(slots=True)
class DocumentModel:
    """
    Root document model.

    This class represents the document as it exists after being read
    from disk, but before any semantic parsing occurs.
    """

    title: str = ""

    paragraph_count: int = 0
    table_count: int = 0

    paragraphs: list[ParagraphModel] = field(default_factory=list)

    def add_paragraph(self, paragraph: ParagraphModel) -> None:
        """
        Adds a paragraph to the document.
        """
        self.paragraphs.append(paragraph)

    def get_paragraph(self, index: int) -> ParagraphModel | None:
        """
        Returns a paragraph by its index.
        """

        if 0 <= index < len(self.paragraphs):
            return self.paragraphs[index]

        return None

    def __len__(self) -> int:
        return len(self.paragraphs)

    def __iter__(self):
        return iter(self.paragraphs)