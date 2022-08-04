"""Employee module"""

import requests


class Employee:
    """A sample Employee class"""
    raise_amt = 1.05  # 5%

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        """Employee email"""
        return f'{self.first_name.lower()}.{self.last_name.lower()}@email.com'

    @property
    def fullname(self):
        """Employee fullname"""
        return f'{self.first_name} {self.last_name}'

    def apply_raise(self):
        """Employee raise"""
        self.pay = int(self.pay * self.raise_amt)

    # Mocking
    def monthly_schedule(self, month):
        """Employee's schedule for a given month"""
        response = requests.get(
            f'http://company.com/{self.last_name.lower()}/{month.lower()}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
