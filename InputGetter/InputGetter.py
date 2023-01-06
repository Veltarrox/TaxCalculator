import sys


class InputGetter:
    @staticmethod
    def get_income():
        try:
            return float(input("Enter income: "))
        except ValueError:
            print("Incorrect Income")
            sys.exit(1)

    @staticmethod
    def get_contract_type():
        try:
            return input("Contract Type: (E)mployment, (C)ivil")[0]
        except IndexError:
            print("Incorrect Contract Type")
            sys.exit(1)
