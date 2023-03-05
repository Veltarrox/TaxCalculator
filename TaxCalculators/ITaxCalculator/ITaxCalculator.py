from abc import ABC, abstractmethod


class ITaxCalculator(ABC):
    @abstractmethod
    def print_results(self) -> None:
        """
        Print results
        :return: None
        """
        pass

    @abstractmethod
    def calculate_taxes(self) -> None:
        """
        Calculate all taxes
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_social_security_tax(self) -> None:
        """
        Calculate social security tax
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_social_security_health_tax(self):
        """
        Calculate social security health tax
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_social_security_sickness_tax(self):
        """
        Calculate social security sickness tax
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_income_basis_for_health_social_security(self):
        """
        Calculate income basis for health social security
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_health_tax_1(self):
        """
        Calculate health tax_1
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_health_tax_2(self):
        """
        Calculate health tax_2
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_tax_free_income(self):
        """
        Calculate tax free income
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_deductible_expenses(self):
        """
        Calculate deductible expenses
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_income_basis_for_advance_tax(self):
        """
        Calculate income basis for advance tax
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_income_basis_for_advance_tax_rounded(self):
        """
        Calculate income basis for advance tax rounded
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_advance_tax_basis(self):
        """
        Calculate advance tax basis
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_advance_tax(self):
        """
        Calculate advance tax
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_advance_tax_rounded(self):
        """
        Calculate advance tax rounded
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_advance_tax_without_free_income(self):
        """
        Calculate advance tax without free income
        :return: None
        """
        pass

    @abstractmethod
    def _calculate_net_income(self):
        """
        Calculate net income
        :return: None
        """
        pass
