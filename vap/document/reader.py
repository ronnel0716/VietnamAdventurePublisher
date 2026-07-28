from docx import Document
from .model import DocumentModel
from .paragraph import Paragraph

class DocumentReader:
    def read(self,path):
        doc=Document(path)
        m=DocumentModel(title=doc.paragraphs[0].text if doc.paragraphs else "")
        for i,p in enumerate(doc.paragraphs):
            m.paragraphs.append(Paragraph(i,p.text,p.style.name))
        return m
