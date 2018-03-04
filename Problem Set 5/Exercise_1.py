"""
Exercise_2
Author: Zander.M
Created at: 12:36, 03, 03, 2018,
"""


def recursive_sum(ls):
	"""split the list into two halves and calculate their sums"""
	if len(ls) == 1:
		return ls[0]
	elif len(ls) == 2:
		return ls[0] + ls[1]
	else:
		i = len(ls) // 2
		left = recursive_sum(ls[:i])
		right = recursive_sum(ls[i:])
		return left + right