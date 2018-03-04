"""
Exercise_3
Author: Zander.M
Created at: 14:03, 03, 03, 2018, 
"""

import pickle

class Employee:
	"""Employ object has four attributes: name, id, dep and title. All of them are str."""
	def __init__(self, name, id_num, department, title):
		d = dict()
		self.name = name
		self.id = id_num
		self.department = department
		self.title = title
		self.d[id_num] = name, department, title

	def change_d(self, name, id_num, department, title):
		self.d[id_num] = name, department, title

def main():

	emp1 = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
	emp2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')
	emp3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')
	emp1 .change_d('Susan Meyers', '47899', 'Programmer', 'Vice President')
	print(Employee.d)
	print(emp1.d)



if __name__ == '__main__':
	main()