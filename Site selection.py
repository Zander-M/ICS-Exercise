"""
Site selection
Author: Zander.M
Created at: 16:06, 03, 06, 2018, 
"""


def site_select(ls):
	"""input is the list of all the coordinate of your friends"""
	a = sorted([i[0] for i in ls])
	b = sorted([j[1] for j in ls])
	return a[len(a) // 2], b[len(b) // 2]