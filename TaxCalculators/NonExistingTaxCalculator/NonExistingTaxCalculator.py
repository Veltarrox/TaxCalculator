from TaxCalculators.DefaultTaxCalculator.DefaultTaxCalculator import DefaultTaxCalculator as DefaultTaxCalculator


class NonExistingTaxCalculator(DefaultTaxCalculator):

    def calculate_taxes(self):
        print("Unknown type of contract!")
