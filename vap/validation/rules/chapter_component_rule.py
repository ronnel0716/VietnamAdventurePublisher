from vap.validation.base_rule import ValidationRule


class ChapterComponentRule(ValidationRule):

    def validate(self, handbook, report):

        for chapter in handbook.chapters:

            if not chapter.components:

                report.warning(
                    "Chapter contains no components.",
                    chapter=chapter.number,
                )