# E1
# in1 = int(input())
# in2 = int(input())
# x = lambda a, b : a if a > b else b
# print(x(in1, in2))
# E2
# name = ''
# for i in input(name):
# 	if i.isupper():
# 		name += i + '.'
# print(name)
# E3
# E4
# E5
# nums = [3, 2, 2, 4]
# val = 3
# a = lambda a: a != val
# ls = list(filter(a, nums))
# print(len(ls))


def parentheses_check(check): # Challenge 1

	st = []
	d = {'}': '{', '>': '<', ']': '[', ')': '('}
	for i in check:
		if i in d.values():
			st.append(i)
		elif i in d.keys():
			if len(st) == 0 or d[i] != st.pop():
				return False
	return True





