from typing import Union

from TaxCalculators.DefaultTaxCalculator.DefaultConstants import *
from TaxCalculators.ITaxCalculator.ITaxCalculator import ITaxCalculator
from TaxCalculators.TaxPrinter.TaxPrinter import TaxPrinter


class DefaultTaxCalculator(ITaxCalculator): # noqa
    _base_income = 0
    _social_security = 0
    _social_security_health = 0
    _social_security_sickness = 0
    _deductible_expenses = 0
    _health_tax_1 = 0
    _health_tax_2 = 0
    _advance_tax_basis = 0
    _tax_free_income = 0
    _advance_tax = 0
    _advance_tax_rounded = 0
    _income_basis_for_health_social_security = 0
    _income_basis_for_advance_tax = 0
    _income_basis_for_advance_tax_rounded = 0
    _advance_tax_without_free_income = 0
    _net_income = 0

    def __init__(self, base_income):
        self._base_income = base_income
        self._tax_printer = TaxPrinter(self)

    @property
    def contract_type(self) -> Union[None, str]:
        return None

    @property
    def base_income(self):
        return self._base_income

    @property
    def social_security(self):
        return self._social_security

    @property
    def social_security_health(self):
        return self._social_security_health

    @property
    def social_security_sickness(self):
        return self._social_security_sickness

    @property
    def income_basis_for_health_social_security(self):
        return self._income_basis_for_health_social_security

    @property
    def health_tax_1(self):
        return self._health_tax_1

    @property
    def health_tax_2(self):
        return self._health_tax_2

    @property
    def deductible_expenses(self):
        return self._deductible_expenses

    @property
    def income_basis_for_advance_tax(self):
        return self._income_basis_for_advance_tax

    @property
    def income_basis_for_advance_tax_rounded(self):
        return self._income_basis_for_advance_tax_rounded

    @property
    def advance_tax_basis(self):
        return self._advance_tax_basis

    @property
    def tax_free_income(self):
        return self._tax_free_income

    @property
    def advance_tax_without_free_income(self):
        return self._advance_tax_without_free_income

    @property
    def advance_tax(self):
        return self._advance_tax

    @property
    def advance_tax_rounded(self):
        return self._advance_tax_rounded

    @property
    def net_income(self):
        return self._net_income

    def print_results(self):
        self._tax_printer.print()

    def calculate_taxes(self) -> None:
        """
        Calculate all taxes
        :return: None
        """
        self._calculate_social_security_tax()
        self._calculate_social_security_health_tax()
        self._calculate_social_security_sickness_tax()
        self._calculate_income_basis_for_health_social_security()
        self._calculate_health_tax_1()
        self._calculate_health_tax_2()
        self._calculate_tax_free_income()
        self._calculate_deductible_expenses()
        self._calculate_income_basis_for_advance_tax()
        self._calculate_income_basis_for_advance_tax_rounded()
        self._calculate_advance_tax_basis()
        self._calculate_advance_tax()
        self._calculate_advance_tax_rounded()
        self._calculate_advance_tax_without_free_income()
        self._calculate_net_income()

    def _calculate_social_security_tax(self) -> None:
        """
        Calculate social security tax
        :return: None
        """
        self._social_security = self._base_income * TaxRates.SOCIAL_SECURITY.value

    def _calculate_social_security_health_tax(self):
        """
        Calculate social security health tax
        :return: None
        """
        self._social_security_health = self._base_income * TaxRates.SOCIAL_SECURITY_HEALTH.value

    def _calculate_social_security_sickness_tax(self):
        """
        Calculate social security sickness tax
        :return: None
        """
        self._social_security_sickness = self._base_income * TaxRates.SOCIAL_SECURITY_SICKNESS.value

    def _calculate_income_basis_for_health_social_security(self):
        """
        Calculate income basis for health social security
        :return: None
        """
        self._income_basis_for_health_social_security = self._base_income - self._social_security - \
                                                        self._social_security_health - self._social_security_sickness

    def _calculate_health_tax_1(self):
        """
        Calculate health tax_1
        :return: None
        """
        self._health_tax_1 = self._income_basis_for_health_social_security * TaxRates.HEALTH_1.value

    def _calculate_health_tax_2(self):
        """
        Calculate health tax_2
        :return: None
        """
        self._health_tax_2 = self._income_basis_for_health_social_security * TaxRates.HEALTH_2.value

    def _calculate_tax_free_income(self):
        """
        Calculate tax free income
        :return: None
        """
        self._tax_free_income = TaxValues.TAX_FREE_INCOME.value

    def _calculate_deductible_expenses(self):
        """
        Calculate deductible expenses
        :return: None
        """
        self._deductible_expenses = TaxValues.DEDUCTIBLE_EXPENSES.value

    def _calculate_income_basis_for_advance_tax(self):
        """
        Calculate income basis for advance tax
        :return: None
        """
        self._income_basis_for_advance_tax = self._income_basis_for_health_social_security - self._deductible_expenses

    def _calculate_income_basis_for_advance_tax_rounded(self):
        """
        Calculate income basis for advance tax rounded
        :return: None
        """
        self._income_basis_for_advance_tax_rounded = float(round(self._income_basis_for_advance_tax, 0))

    def _calculate_advance_tax_basis(self):
        """
        Calculate advance tax basis
        :return: None
        """
        self._advance_tax_basis = self._income_basis_for_advance_tax_rounded * TaxRates.ADVANCE.value

    def _calculate_advance_tax(self):
        """
        Calculate advance tax
        :return: None
        """
        self._advance_tax = self._advance_tax_basis - self._health_tax_2 - self._tax_free_income

    def _calculate_advance_tax_rounded(self):
        """
        Calculate advance tax rounded
        :return: None
        """
        self._advance_tax_rounded = float(round(self._advance_tax, 0))

    def _calculate_advance_tax_without_free_income(self):
        """
        Calculate advance tax without free income
        :return: None
        """
        self._advance_tax_without_free_income = self._advance_tax_basis - self._tax_free_income

    def _calculate_net_income(self):
        """
        Calculate net income
        :return: None
        """
        self._net_income = self._base_income - (self._social_security + self._social_security_health +
                                                self._social_security_sickness + self._health_tax_1 +
                                                self._advance_tax_rounded)
