class TaxPrinter:

    def __init__(self, tax_calculator):
        self._tax_calculator = tax_calculator

    def print(self):
        """
        Print all taxes information
        """
        if self._tax_calculator.contract_type:
            self._print_contract_type()
            self._print_base_income()
            self._print_social_security_tax()
            self._print_health_social_security_tax()
            self._print_sickness_social_security_tax()
            self._print_income_basis_for_health_social_security()
            self._print_health_taxes()
            self._print_deductible_expenses()
            self._print_income_basis_for_advance_tax()
            self._print_advance_tax_basis()
            self._print_tax_free_income()
            self._print_advance_tax_without_free_income()
            self._print_advance_tax()
            self._print_net_income()
        else:
            print("Unknown type of contract!")

    @staticmethod
    def _round_to_two_trailing_zeroes(number):
        return "{0:.2f}".format(number)

    @staticmethod
    def _round_to_whole_number(number):
        return "{0:.0f}".format(number)

    def _print_contract_type(self):
        if self._tax_calculator.contract_type:
            print(f"\n{self._tax_calculator.contract_type}\n")
        else:
            pass

    def _print_base_income(self):
        print("Base Income ", self._tax_calculator.base_income)

    def _print_social_security_tax(self):
        print("Social security tax: " + self._round_to_two_trailing_zeroes(self._tax_calculator.social_security))

    def _print_health_social_security_tax(self):
        print("Health social security tax: " + self._round_to_two_trailing_zeroes(
            self._tax_calculator.social_security_health))

    def _print_sickness_social_security_tax(self):
        print("Sickness social security tax: " + self._round_to_two_trailing_zeroes(
            self._tax_calculator.social_security_sickness))

    def _print_income_basis_for_health_social_security(self):
        print("Income basis for health social security tax: ",
              self._tax_calculator.income_basis_for_health_social_security)

    def _print_health_taxes(self):
        print("Health social security tax: 9% = " + self._round_to_two_trailing_zeroes(
            self._tax_calculator.health_tax_1) + " 7,75% = " +
              self._round_to_two_trailing_zeroes(self._tax_calculator.health_tax_2))

    def _print_deductible_expenses(self):
        print("Tax deductible expenses: ", self._tax_calculator.deductible_expenses)

    def _print_income_basis_for_advance_tax(self):
        print("Income basis for advance tax: ",
              self._round_to_two_trailing_zeroes(self._tax_calculator.income_basis_for_advance_tax),
              " rounded: " + self._round_to_whole_number(self._tax_calculator.income_basis_for_advance_tax_rounded))

    def _print_advance_tax_basis(self):
        print("Advance tax 18% = ", self._round_to_two_trailing_zeroes(self._tax_calculator.advance_tax_basis))

    def _print_tax_free_income(self):
        print("Tax free income =", self._tax_calculator.tax_free_income)

    def _print_advance_tax_without_free_income(self):
        print("Advance tax without free income = " +
              self._round_to_two_trailing_zeroes(self._tax_calculator.advance_tax_without_free_income))

    def _print_advance_tax(self):
        print("Advance tax actually paid = " + self._round_to_two_trailing_zeroes(self._tax_calculator.advance_tax)
              + " rounded " + self._round_to_whole_number(self._tax_calculator.advance_tax_rounded))

    def _print_net_income(self):
        print("Net income = " + self._round_to_two_trailing_zeroes(self._tax_calculator.net_income))
