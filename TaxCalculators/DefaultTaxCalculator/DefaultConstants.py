from enum import Enum


class TaxRates(Enum):
    """
    Tax Rates as a number, not percents
    """

    SOCIAL_SECURITY = 0.0976
    SOCIAL_SECURITY_HEALTH = 0.015
    SOCIAL_SECURITY_SICKNESS = 0.0245
    HEALTH_1 = 0.09
    HEALTH_2 = 0.0775
    ADVANCE = 0.18


class TaxValues(Enum):
    """
    Values in PLN
    """
    TAX_FREE_INCOME = 46.33
    DEDUCTIBLE_EXPENSES = 111.25
