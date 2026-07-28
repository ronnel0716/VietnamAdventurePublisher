import re

class ChapterDetector:
    PATTERN = re.compile(r"^CHAPTER\s+(\d+)$", re.I)

    def detect(self, document):
        chapters=[]
        current=None
        for p in document.paragraphs:
            m=self.PATTERN.match(p.text.strip())
            if not m:
                continue
            if current:
                current["end"]=p.index-1
            current={"number":int(m.group(1)),
                     "title":"Untitled",
                     "start":p.index,
                     "end":len(document.paragraphs)-1}
            chapters.append(current)
        return chapters
