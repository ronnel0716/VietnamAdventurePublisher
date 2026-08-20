from dataclasses import dataclass


@dataclass(slots=True)
class ValidationIssue:

    severity: str
    message: str

    chapter: int | None = None

    component: int | None = None