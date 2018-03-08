# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:41:14 2017

@author: Mebius
"""


def permute(nums):
    if len(nums) == 0: 
        return [[]]
    if len(nums) == 1: 
        return [nums]
    pattern = permute(nums[1:])
    c = []
    for i in range(len(nums)):
        for p in pattern:
            c.append(p[:i] + [nums[0]] + p[i:])
    
    return c
    
def main():
    num_list = [1,2,3]
    print(permute(num_list))    
main()