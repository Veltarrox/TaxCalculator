from TaxCalculators.DefaultTaxCalculator.DefaultTaxCalculator import DefaultTaxCalculator
from TaxCalculators.CivilTaxCalculator.CivilConstants import TaxRates


class CivilTaxCalculator(DefaultTaxCalculator):

    def __init__(self, base_income):
        super().__init__(base_income)

    @property
    def contract_type(self) -> str:
        return "CIVIL"

    def _calculate_tax_free_income(self):
        self._tax_free_income = 0

    def _calculate_deductible_expenses(self):
        self._deductible_expenses = self._income_basis_for_health_social_security * TaxRates.DEDUCTIBLE_EXPENSES.value

    def _calculate_advance_tax_without_free_income(self):
        self._advance_tax_without_free_income = self._advance_tax_basis
