# exercise 1
# def maximum(ls):
# 	if len(ls) == 1:
# 		return ls[0]
# 	elif len(ls) == 2:
# 		if ls[0] > ls[1]:
# 			return ls[0]
# 		else:
# 			return ls[1]
# 	else:
# 		n = len(ls) // 2
# 		left = ls[:n]
# 		right = ls[n:]
# 		if maximum(left) > maximum(right):
# 			return maximum(left)
# 		else:
# 			return maximum(right)
#
# print(maximum([999988999, 6666, 6666, 666, 45, 12, 56456, 465]))

class PersonalInformation:
	def __init__(self, address, age, phone):
		self.address = address
		self.age = age
		self.phone = phone

man1 = PersonalInformation('adfdafd', 'fkdlajfkldasjf', 'fjdsajfkldjask')
Jerry = PersonalInformation('huangpu','26', 123456789)
print(Jerry.address)
