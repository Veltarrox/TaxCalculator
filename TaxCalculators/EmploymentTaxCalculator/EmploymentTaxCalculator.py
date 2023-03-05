from TaxCalculators.DefaultTaxCalculator.DefaultTaxCalculator import DefaultTaxCalculator as DefaultTaxCalculator


class EmploymentTaxCalculator(DefaultTaxCalculator):

    def __init__(self, base_income):
        super().__init__(base_income)

    @property
    def contract_type(self) -> str:
        return "EMPLOYMENT"
