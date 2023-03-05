from TaxCalculators.EmploymentTaxCalculator.EmploymentTaxCalculator import EmploymentTaxCalculator
from TaxCalculators.CivilTaxCalculator.CivilTaxCalculator import CivilTaxCalculator
from TaxCalculators.ITaxCalculator.ITaxCalculator import ITaxCalculator
from TaxCalculators.NonExistingTaxCalculator.NonExistingTaxCalculator import NonExistingTaxCalculator


class TaxCalculatorCreator:

    @staticmethod
    def create_tax_calculator(contract_type, base_income) -> ITaxCalculator:
        """
        Return instance of class

        :param base_income: base income
        :param contract_type: type of contract
        :return: tax calcultor
        """
        if contract_type == "E":
            return EmploymentTaxCalculator(base_income)
        elif contract_type == "C":
            return CivilTaxCalculator(base_income)
        else:
            return NonExistingTaxCalculator(base_income)
