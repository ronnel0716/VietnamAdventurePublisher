"""
reader.py

Reads a DOCX file and converts it into the application's
DocumentModel.
"""

from __future__ import annotations

from docx import Document

from vap.models.document import DocumentModel
from vap.models.paragraph import ParagraphModel


class DocumentReader:
    """
    Reads Microsoft Word documents.
    """

    def read(self, path) -> DocumentModel:

        doc = Document(path)

        model = DocumentModel()

        if doc.paragraphs:
            model.title = doc.paragraphs[0].text

        model.table_count = len(doc.tables)

        for index, paragraph in enumerate(doc.paragraphs):

            p = ParagraphModel()

            if hasattr(p, "index"):
                p.index = index

            if hasattr(p, "text"):
                p.text = paragraph.text

            if hasattr(p, "style"):
                p.style = paragraph.style.name

            model.add_paragraph(p)

        model.paragraph_count = len(model)

        return model