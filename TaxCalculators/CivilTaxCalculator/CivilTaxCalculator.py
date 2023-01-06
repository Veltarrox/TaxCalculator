from TaxCalculators.FormattingVersions.FormattingVersions import round_to_two_trailing_zeroes
from TaxCalculators.DefaultTaxCalculator.DefaultTaxCalculator import DefaultTaxCalculator
from TaxCalculators.CivilTaxCalculator.CivilConstants import DEDUCTIBLE_EXPENSES_RATE


class CivilTaxCalculator(DefaultTaxCalculator):

    def _calculate_tax_free_income(self):
        self._tax_free_income = 0

    def _calculate_deductible_expenses(self):
        self._deductible_expenses = self._income_basis_for_health_social_security * DEDUCTIBLE_EXPENSES_RATE

    def _calculate_advance_tax_without_free_income(self):
        self._advance_tax_without_free_income = self._advance_tax_basis

    def _print_contract_type(self):
        print("CIVIL")

    def _print_tax_free_income(self):
        pass

    def _print_advance_tax_without_free_income(self):
        print("Already paid tax = " + round_to_two_trailing_zeroes(self._advance_tax_without_free_income))
