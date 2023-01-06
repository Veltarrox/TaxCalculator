from TaxCalculators.TaxCalculatorPicker import tax_calculator_picker
from TaxCalculators.TaxCalculators import TAX_CALCULATORS
from InputGetter.InputGetter import InputGetter


def main():
    base_income = InputGetter.get_income()
    contract_type = InputGetter.get_contract_type()
    contract = TAX_CALCULATORS[tax_calculator_picker(contract_type)](base_income)
    contract.calculate_taxes()


if __name__ == '__main__':
    main()
