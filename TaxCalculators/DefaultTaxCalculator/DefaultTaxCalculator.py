from TaxCalculators.DefaultTaxCalculator.DefaultConstants import *
from TaxCalculators.FormattingVersions.FormattingVersions import round_to_whole_number, round_to_two_trailing_zeroes


class DefaultTaxCalculator:
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

    def calculate_taxes(self):
        self._calculate_results()
        self._print_results()

    def _calculate_results(self):
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

    def _print_results(self):
        self._print_contract_type()
        self._print_base_income()
        self._print_social_security_tax()
        self._print_health_social_security_tax()
        self._print_sickness_social_security_tax()
        self._print_income_basis_for_health_social_security()
        self._print_health_taxes()
        self._print_deductible_expenses()
        self._print_income_basis_for_advance_tax()
        self._print_advance_tax_basis()
        self._print_tax_free_income()
        self._print_advance_tax_without_free_income()
        self._print_advance_tax()
        self._print_net_income()

    def _calculate_social_security_tax(self):
        self._social_security = self._base_income * SOCIAL_SECURITY_TAX_RATE

    def _calculate_social_security_health_tax(self):
        self._social_security_health = self._base_income * SOCIAL_SECURITY_HEALTH_TAX_RATE

    def _calculate_social_security_sickness_tax(self):
        self._social_security_sickness = self._base_income * SOCIAL_SECURITY_SICKNESS_TAX_RATE

    def _calculate_income_basis_for_health_social_security(self):
        self._income_basis_for_health_social_security = self._base_income - self._social_security - \
                                                        self._social_security_health - self._social_security_sickness

    def _calculate_health_tax_1(self):
        self._health_tax_1 = self._income_basis_for_health_social_security * HEALTH_TAX_1_RATE

    def _calculate_health_tax_2(self):
        self._health_tax_2 = self._income_basis_for_health_social_security * HEALTH_TAX_2_RATE

    def _calculate_tax_free_income(self):
        self._tax_free_income = TAX_FREE_INCOME

    def _calculate_deductible_expenses(self):
        self._deductible_expenses = DEDUCTIBLE_EXPENSES

    def _calculate_income_basis_for_advance_tax(self):
        self._income_basis_for_advance_tax = self._income_basis_for_health_social_security - self._deductible_expenses

    def _calculate_income_basis_for_advance_tax_rounded(self):
        self._income_basis_for_advance_tax_rounded = float(round_to_whole_number(self._income_basis_for_advance_tax))

    def _calculate_advance_tax_basis(self):
        self._advance_tax_basis = self._income_basis_for_advance_tax_rounded * ADVANCE_TAX_RATE

    def _calculate_advance_tax(self):
        self._advance_tax = self._advance_tax_basis - self._health_tax_2 - self._tax_free_income

    def _calculate_advance_tax_rounded(self):
        self._advance_tax_rounded = float(round_to_whole_number(self._advance_tax))

    def _calculate_advance_tax_without_free_income(self):
        self._advance_tax_without_free_income = self._advance_tax_basis - self._tax_free_income

    def _calculate_net_income(self):
        self._net_income = self._base_income - (self._social_security + self._social_security_health +
                                                self._social_security_sickness + self._health_tax_1 +
                                                self._advance_tax_rounded)

    def _print_contract_type(self):
        pass

    def _print_base_income(self):
        print("Base Income ", self._base_income)

    def _print_social_security_tax(self):
        print("Social security tax: " + round_to_two_trailing_zeroes(self._social_security))

    def _print_health_social_security_tax(self):
        print("Health social security tax: " + round_to_two_trailing_zeroes(self._social_security_health))

    def _print_sickness_social_security_tax(self):
        print("Sickness social security tax: " + round_to_two_trailing_zeroes(self._social_security_sickness))

    def _print_income_basis_for_health_social_security(self):
        print("Income basis for health social security tax: ", self._income_basis_for_health_social_security)

    def _print_health_taxes(self):
        print("Health social security tax: 9% = " + round_to_two_trailing_zeroes(self._health_tax_1) + " 7,75% = " +
              round_to_two_trailing_zeroes(self._health_tax_2))

    def _print_deductible_expenses(self):
        print("Tax deductible expenses: ", self._deductible_expenses)

    def _print_income_basis_for_advance_tax(self):
        print("Income basis for advance tax: ", round_to_two_trailing_zeroes(self._income_basis_for_advance_tax),
              " rounded: " + round_to_whole_number(self._income_basis_for_advance_tax_rounded))

    def _print_advance_tax_basis(self):
        print("Advance tax 18% = ", round_to_two_trailing_zeroes(self._advance_tax_basis))

    def _print_tax_free_income(self):
        print("Tax free income =", self._tax_free_income)

    def _print_advance_tax_without_free_income(self):
        print("Advance tax without free income = " +
              round_to_two_trailing_zeroes(self._advance_tax_without_free_income))

    def _print_advance_tax(self):
        print("Advance tax actually paid = " + round_to_two_trailing_zeroes(self._advance_tax) + " rounded " +
              round_to_whole_number(self._advance_tax_rounded))

    def _print_net_income(self):
        print()
        print("Net income = " + round_to_two_trailing_zeroes(self._net_income))
