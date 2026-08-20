from vap.validation.report import ValidationReport

from vap.validation.rules.handbook_title_rule import HandbookTitleRule
from vap.validation.rules.chapter_component_rule import ChapterComponentRule


class HandbookValidator:

    def __init__(self):

        self.rules = [
            HandbookTitleRule(),
            ChapterComponentRule(),
        ]

    def validate(self, handbook):

        report = ValidationReport()

        for rule in self.rules:
            rule.validate(handbook, report)

        return report