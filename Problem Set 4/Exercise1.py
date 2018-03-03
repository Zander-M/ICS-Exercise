def permute(nums):
	ls = []
	if len(nums) == 2:
		return num, num[::-1]
	elif len(nums) == 1:
		return nums
	else:
		return nums.extend(permute(nums))
	return ls



