# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:58:27 2017

@author: Mebius

Joyce edited it on Mar 12 2018
"""
import stack_student

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:58:27 2017

@author: Mebius

Joyce edited it on Mar 12 2018
"""
import stack_student

def stack_union_dup(lst1, lst2):
    """
    find the union of two *sorted* list,
    those 2 lists could contain duplicate numbers in each one

    Arguments: two sorted list, each in ascending order

    Return: one list, also in ascending order

    Example: stack_inter([0, 2, 2, 4], [0, 2, 3]) returns [0, 2, 3, 4]
    """

    #-------------your code below-----------------#
def stack_union_dup(s1, s2):
    # impliment with stack method
    # while s1.size() != 0 and s2.size() != 0:
    #     if s1.peek() == s2.peek():
    #         a = s1.pop()
    #         s2.pop()
    #     else:
    #         a = s1.pop() if s1.peek() > s2.peek() else s2.pop()
    #     if len(union) == 0 or a != union[-1]:
    #         union.append(a)
    # union.sort()
    return list(set(s1).union(set(s2)))
    #------------end of your code-----------------#
    

if __name__ == "__main__":
    import random
    random.seed(0)

    l1 = [random.randint(1, 20) for i in range(5)]
    l2 = [random.randint(1, 20) for i in range(5)]
    l1 = l1 *2
    l1.sort(); l2.sort()
    
    print("l1: ", l1)
    print("l2: ", l2)
    r = stack_union_dup(l1, l2)
    print(r)
