from TaxCalculators.TaxCalculatorPicker import TaxCalculatorCreator
from InputGetter.InputGetter import InputGetter


def main():
    base_income = InputGetter.get_income()
    contract_type = InputGetter.get_contract_type()

    tax_calculator = TaxCalculatorCreator().create_tax_calculator(contract_type, base_income)
    tax_calculator.calculate_taxes()
    tax_calculator.print_results()


if __name__ == '__main__':
    main()
