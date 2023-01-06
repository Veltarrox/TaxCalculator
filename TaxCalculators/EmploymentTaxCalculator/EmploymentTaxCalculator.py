from TaxCalculators.DefaultTaxCalculator.DefaultTaxCalculator import DefaultTaxCalculator as DefaultTaxCalculator


class EmploymentTaxCalculator(DefaultTaxCalculator):

    def _print_contract_type(self):
        print("EMPLOYMENT")
