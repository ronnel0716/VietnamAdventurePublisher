from .chapter_detector import ChapterDetector

class HandbookBuilder:
    def build(self, document):
        return {
            "title": document.title,
            "chapters": ChapterDetector().detect(document)
        }
