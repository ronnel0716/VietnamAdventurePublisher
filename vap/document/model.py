from dataclasses import dataclass, field
from .paragraph import Paragraph

@dataclass
class DocumentModel:
    title:str=""
    paragraphs:list[Paragraph]=field(default_factory=list)
