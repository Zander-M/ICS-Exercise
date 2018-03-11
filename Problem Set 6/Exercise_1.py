"""
Exercise_1.py
Author: Zander.M
Created at: 13:18, 03, 09, 2018, 
"""

"this program creates a class for bank management"


class Account:
	__number = 0

	def __init__(self, name, acc_type, balance):
		self.name = name
		self.number = self.__number
		self.acc_type = acc_type
		self.balance = balance

	def get_holder(self):
		return self.name

	def get_balance(self):
		return self.balance

	def compound_interest(self, year):
		if self.acc_type == 'C':
			ratio = 0.08
		else:
			ratio = 0.04
		return self.balance * (1 + ratio) ** year - self.balance

class Customer:
	__number = 0

	def __init__(self, name, acc_type, balance):
		self.name = name
		self.account = Account(name=name, acc_type=acc_type, balance=balance)


new_c = Customer("Michael", "C", 20000)

print(new_c.account.get_holder())
print(new_c.account.get_balance())
print(new_c.account.compound_interest(10))
