'''this program return the next permutation according to lexicographical order'''
def next_permute(curr_perm):
	a = [curr_perm[-1]]
	for i in range(len(curr_perm) - 2, -1, -1):
		if curr_perm[i] < a[-1]:
			a.append(curr_perm[i])
			a.sort()
			return curr_perm[:i] + [a.pop(a.index(curr_perm[i]) + 1)] + a
		else:
			a.append(curr_perm[i])
	return curr_perm[::-1]
