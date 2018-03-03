#Sorting Methods

#  bubble sort
# def bubble_sort(ls):
# 	flag = 1
# 	while flag == 1:
# 		flag = 0
# 		for i in range(len(ls) - 1):
# 			if ls[i] > ls[i + 1]:
# 				flag = 1
# 				ls[i], ls[i+1] = ls[i+1], ls[i]
# 	return ls

# bubble sort opt1
# def bubble_sort(ls):
# 	for i in range(len(ls)):
# 		for j in range(len(ls) - 1 - i):
# 			if ls[j] > ls[j + 1]:
# 				ls[j], ls[j + 1] = ls[j + 1], ls[j]
# 	return ls
#
# print(bubble_sort([2,1,3,4,5,7,6,8]))

# Merge Sort


# def merge_sort(ls):
# 	if len(ls) <= 1:
# 		return ls
# 	else:
# 		i = len(ls) // 2
# 		left = merge_sort(ls[:i]) # using recursion here
# 		right = merge_sort(ls[i:]) # using recursion here
# 	return merge(left, right)
#
#
# def merge(left, right):
# 	result = []
# 	while len(left) != 0 and len(right) != 0:
# 		if left[0] < right[0]:
# 			result.append(left.pop(0))
# 		else:
# 			result.append(right.pop(0))
# 	return result + left + right
#
#
# print(merge_sort([2, 7, 4, 5, 3, 6, 1]))

