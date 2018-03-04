"""
Exercise_2
Author: Zander.M
Created at: 12:36, 03, 03, 2018,
"""

class Employee:
	"""Employ object has four attributes: name, id, dep and title. All of them are str."""
	def __init__(self, name, id, department, title):
		self.name = name
		self.id = id
		self.dep = department
		self.title = title


def main():
	emp1 = Employee('Susan Meyers', '47899', 'Accoundting', 'Vice President')
	emp2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')
	emp3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')
	print(emp1.__dict__)
	print(emp2.__dict__)
	print(emp3.__dict__)


if __name__ == '__main__':
	main()