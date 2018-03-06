# def permute(nums): '''unsuccessful attempt using recursion''
# 	ans = []
# 	if len(nums) == 1:
# 		return nums
# 	else:
# 		for i in nums:
# 			a = nums[:]
# 			c = [a.pop(a.index(i))]
# 			b = permute(a)
# 			ans.extend(c + b)
# 		return ans
'''this program returns all the permutations of a list of integers.'''
import time

def timeit(f, *args):
    t1 = time.time()
    f(*args)
    t2 = time.time()
    return t2 - t1


def permute(nums):
	ls = [[]]
	new_ls = []
	for i in nums:
		for j in ls:
			for k in range(len(ls[0]) + 1):
				new_ls.append( j[:k] + [i] + j[k:])
		ls = new_ls[:]
		new_ls = []
	return ls



print(timeit(permute,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


