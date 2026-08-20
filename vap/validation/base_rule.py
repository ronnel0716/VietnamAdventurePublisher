from abc import ABC, abstractmethod

from vap.validation.report import ValidationReport


class ValidationRule(ABC):
    """
    Base class for all validation rules.
    """

    @abstractmethod
    def validate(self, handbook, report: ValidationReport):
        """Validate the handbook and add issues to the report."""
        raise NotImplementedError