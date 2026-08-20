from vap.validation.base_rule import ValidationRule


class HandbookTitleRule(ValidationRule):

    def validate(self, handbook, report):

        if not handbook.title.strip():
            report.error(
                "Handbook title is missing."
            )