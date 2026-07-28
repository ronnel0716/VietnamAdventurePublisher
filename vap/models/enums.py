from enum import Enum, auto


class ComponentType(Enum):
    UNKNOWN = auto()

    QUICK_FACTS = auto()
    TRAVEL_TIP = auto()
    EDITORS_NOTE = auto()
    BUDGET_TIP = auto()
    SENIOR_ADVICE = auto()
    CAUTION = auto()

    CHECKLIST = auto()
    TIMELINE = auto()

    TABLE = auto()
    IMAGE = auto()
    QR_CODE = auto()

    PARAGRAPH = auto()