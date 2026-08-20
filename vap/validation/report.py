from dataclasses import dataclass, field

from .issue import ValidationIssue


@dataclass(slots=True)
class ValidationReport:

    issues: list[ValidationIssue] = field(default_factory=list)

    def error(self, message, chapter=None, component=None):

        self.issues.append(
            ValidationIssue(
                severity="ERROR",
                message=message,
                chapter=chapter,
                component=component,
            )
        )

    def warning(self, message, chapter=None, component=None):

        self.issues.append(
            ValidationIssue(
                severity="WARNING",
                message=message,
                chapter=chapter,
                component=component,
            )
        )

    @property
    def errors(self):

        return [
            i
            for i in self.issues
            if i.severity == "ERROR"
        ]

    @property
    def warnings(self):

        return [
            i
            for i in self.issues
            if i.severity == "WARNING"
        ]

    @property
    def valid(self):

        return len(self.errors) == 0