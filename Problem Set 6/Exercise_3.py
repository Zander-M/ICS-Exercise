"""
Exercise_3
Author: Zander.M
Created at: 10:35, 03, 11, 2018, 
"""


class RetailItem:
	ls = []

	def __init__(self, des, unit, price):
		self.description = des
		self.unit = unit
		self.price = price
		self.ls.append(self)


Item1 = RetailItem("Jacket", 12, 59.95)
Item2 = RetailItem("Designer Jeans", 40, 34.95)
Item3 = RetailItem("Shirt", 20, 24.95)


class CashRegister:
	ls = []

	def purchase_item(self, retail):
		"""accepts a retail item"""
		self.ls.append(retail)

	def get_total(self):
		return sum([i.price for i in self.ls])

	def show_items(self):
		print([(l.description,l.price) for l in self.ls])

	def clear(self):
		self.ls = []


def main():
	reg = CashRegister()
	item = input('Please input the thing you want to purchase,\
terminate input "0".')
	while item != "0":
		for k in RetailItem.ls:
			if k.description == item:
				reg.purchase_item(k)
		item = input('Please input the thing you want to purchase,\
terminate input "0".')
	reg.show_items()
	reg.clear()


if __name__ == '__main__':
	main()
