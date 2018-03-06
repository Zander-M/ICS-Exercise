"""
Shortest_Sum
Author: Zander.M
Created at: 17:31, 03, 06, 2018, 
"""


def smallest_sum(ls):
	"""this program returns the smallest sum of a triangular list.
	Example: [1], [2, 5], [6, 7, 3], [4, 5, 7, 9]"""
	sm = ls[-1][:]
	res = []
	for i in range(len(ls) - 2, -1, -1):
		for j in range(len(ls[i])):
			res.append(min(ls[i][j] + sm[j], ls[i][j] + sm[j + 1]))
		sm = res[:]
		res = []

	return min(sm)


print(smallest_sum([[1], [2, 5], [6, 7, 3], [4, 5, 7, 9]]))



