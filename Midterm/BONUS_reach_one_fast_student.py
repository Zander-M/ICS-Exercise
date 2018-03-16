# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:58:27 2018

@author: Joyce

"""

def reach_one_fast(n, m = {}):
    """n is a positive integer.
    find the *min* number of steps to reduce n to 1 by four types of operations
    
    1. subtract 1 from n
    2. if n can be evenly divided by 4, then n/4
    3. if n can be evenly divided by 3, then n/3
    4. if n can be evenly divided by 2, then n/2
    
    return the min number of steps

    Example: reach_one(1) prints 0, reach_one(4) prints 2
    """
    
    m[1] = 0
    try:
        return m[n]

    #-------------your code below-----------------#
    except KeyError:
        if n % 4 == 0:
            m[n] = reach_one_fast(n // 4, m) + 1
            return m[n]
        elif n % 3 == 0:
            m[n] = reach_one_fast(n // 3, m) + 1
            return m[n]
        elif n % 2 == 0:
            m[n] = reach_one_fast(n // 2, m) + 1
            return m[n]
        else:
            m[n] = reach_one_fast(n - 1, m) + 1
            return m[n]




if __name__ == "__main__":
    print(reach_one_fast(1))
    print(reach_one_fast(4))
    print(reach_one_fast(16))
