"""
colors.py

Central color definitions used by the publisher.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:

    BLACK = "000000"
    WHITE = "FFFFFF"

    GRAY_100 = "F8F9FA"
    GRAY_200 = "E9ECEF"
    GRAY_300 = "DEE2E6"
    GRAY_400 = "CED4DA"
    GRAY_500 = "ADB5BD"

    BLUE = "0D6EFD"
    GREEN = "198754"
    ORANGE = "FD7E14"
    RED = "DC3545"
    YELLOW = "FFC107"

    TRAVEL_TIP = GREEN
    QUICK_FACTS = BLUE
    EDITORS_NOTE = ORANGE
    BUDGET_TIP = GREEN
    SENIOR_ADVICE = BLUE
    CAUTION = RED