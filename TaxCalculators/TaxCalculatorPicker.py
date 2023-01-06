from TaxCalculators.EmploymentTaxCalculator.EmploymentTaxCalculator import EmploymentTaxCalculator
from TaxCalculators.CivilTaxCalculator.CivilTaxCalculator import CivilTaxCalculator
from TaxCalculators.NonExistingTaxCalculator.NonExistingTaxCalculator import NonExistingTaxCalculator


def tax_calculator_picker(contract_type):
    if contract_type == "E":
        picked_tax_calculator = EmploymentTaxCalculator.__name__
    elif contract_type == "C":
        picked_tax_calculator = CivilTaxCalculator.__name__
    else:
        picked_tax_calculator = NonExistingTaxCalculator.__name__
    return picked_tax_calculator
