# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:58:27 2018

@author: Joyce

"""

def reach_one(n):
    """n is a positive integer.
    find the *min* number of steps to reduce n to 1 by 2 types of operations
    
    1. subtract 1 from n
    2. if n can be evenly divided by 2, then do n/2
    
    return the min number of steps

    Example: reach_one(1) prints 0, reach_one(4) prints 2
    """
    if n == 1:
        return 0
    #-------------your code below-----------------#
    elif n % 2 == 0:
        return reach_one(n // 2) + 1
    else:
       return reach_one(n-1) + 1




if __name__ == "__main__":
    
    print(reach_one(1))
    print(reach_one(4))
    print(reach_one(16))
