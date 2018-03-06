# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:41:14 2017

@author: Mebius
"""
import time

def timeit(f, *args):
    t1 = time.time()
    f(*args)
    t2 = time.time()
    return t2 - t1

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
    # num_list = [1,2,3]
    print(timeit(permute, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


main()