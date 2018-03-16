# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:58:27 2017

@author: Mebius

Joyce edited it on Mar 12 2018
"""
import stack_student

def stack_inter(lst1, lst2):
    """
    find the intersection of two *sorted* list, with no duplicate

    Arguments: two sorted list, each in ascending order

    Return: one list, also in ascending order

    Example: stack_inter([0, 1], [0, 2, 4]) returns [0]
    """
    s1 = stack_student.Stack()
    s1.push_list(lst1)
    s2 = stack_student.Stack()
    s2.push_list(lst2)
    inter = []

    #-------------your code below-----------------#
    while s1.size() != 0 and s2.size() != 0:
        if s1.peek() == s2.peek():
            inter.append(s1.pop())
        else:
            s1.pop() if s1.peek() > s2.peek() else s2.pop()

    #------------end of your code-----------------#
    return inter

if __name__ == "__main__":
    import random
    random.seed(0)

    l1 = [random.randint(1, 20) for i in range(5)]
    l2 = [random.randint(1, 20) for i in range(5)]
    l1.sort(); l2.sort()
    
    print("l1: ", l1)
    print("l2: ", l2)
    r = stack_inter(l1, l2)
    print(r)
