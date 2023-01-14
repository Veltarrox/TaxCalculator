from TaxCalculators.DefaultTaxCalculator.DefaultTaxCalculator import DefaultTaxCalculator as DefaultTaxCalculator


class NonExistingTaxCalculator(DefaultTaxCalculator):

    def __init__(self, base_income):
        super().__init__(base_income)

    @property
    def contract_type(self) -> None:
        return None

    def calculate_taxes(self):
        pass