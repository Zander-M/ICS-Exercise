# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 16:28:13 2016

@author: Mebius
"""

import matplotlib.pyplot as plt
import math
import time

#you can define the limit of n here
LIMIT = 500000

def fast_fib(n, memo={}):
    #assume n is a non-negative integer, and the function returns Fib of n
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fast_fib(n-1, memo)+fast_fib(n-2, memo)
        memo[n] = result
        return result
        

def check_func_time(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time
    
my_range = list(range(1,LIMIT))
a = [check_func_time(fast_fib, number) for number in my_range]

plt.plot(my_range, a, 'r-', label = 'Fib') 
