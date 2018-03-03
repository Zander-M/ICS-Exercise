# def permute(nums):
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






