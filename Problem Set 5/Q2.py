# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:52:11 2017

@author: Mebius
"""

def next_permute(nums):

    split_pos = -1
    for i in range(len(nums)-1, 0, -1):
        if nums[i-1] < nums[i]:
            split_pos = i   
            break
    if split_pos < 0:
        nums.reverse()
    else:
        for i in range(len(nums)-1, split_pos-1, -1):
            if nums[i] > nums[split_pos-1]:
                nums[i], nums[split_pos-1] = nums[split_pos-1], nums[i]
                break
    nums[split_pos:].sort()
    return nums
    
def main():
    num = [1,4,3,2]
    print(next_permute(num))
    
main()