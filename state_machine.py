# ope = [ '+', '-', '*', "/"]
# while input != "q":
# 	a = input()
# 	if not a.isdigit():
# 		if a == 'q':
# 			break
# 		elif a == 'c':
# 			a = input()
# 		else:
# 			a = input()
# 	b = input()
# 		if not b.isdigit():
# 			if b == 'q':
# 				break
# 			elif b == 'c':
# 				b = input()
# 			else:
# 				b = input()
# 		c = input()
# 		if c not in ope:
# 			if c == 'q'
# 				break
# 			elif b == 'c':
# 				b = input()
# 			else:
# 				b = input()
#

def first_num(a):
	while not a.isdigit():
		a = input()
		if a == 'q':
			return False
	return a


def second_num(b):
	while not b.isdigit():
		b = input()
		if b == 'q':
			return False
		elif  b == 'c':
			return True
	return b

def ope(c):
	while not c.isdigit():
		pass
	return



