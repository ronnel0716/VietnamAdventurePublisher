from dataclasses import dataclass

@dataclass(slots=True)
class Paragraph:
    index:int
    text:str
    style:str
