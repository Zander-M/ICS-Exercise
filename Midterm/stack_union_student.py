# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:58:27 2017

@author: Mebius

Joyce edited it on Mar 12 2018
"""

import stack_student


def stack_union(lst1, lst2):
    """find the union of two *sorted* lists, with no duplicate in them

    Arguments: two sorted lists, each in ascending order

    Return: one list, also in *ascending* order

    Example: stack_union([0, 1], [0, 2, 4]) returns [0, 1, 2, 4]
    """
    s1 = stack_student.Stack()
    s1.push_list(lst1)
    s2 = stack_student.Stack()
    s2.push_list(lst2)
    union = []

    #-------------your code below-----------------#
    while s1.size() != 0 and s2.size() != 0:
        if s1.peek() == s2.peek():
            a = s1.pop()
            s2.pop()
        else:
            a = s1.pop() if s1.peek() > s2.peek() else s2.pop()
        if len(union) == 0 or a != union[-1]:
            union.append(a)
    union.sort()
    #------------end of your code-----------------#
    return s1.items + union if s1.size != 0 else s2.items + union

if __name__ == "__main__":
    import random
    random.seed(0)

    l1 = [random.randint(1, 20) for i in range(5)]
    l2 = [random.randint(1, 20) for i in range(5)]
    l1.sort(); l2.sort()

    print("l1: ", l1)
    print("l2: ", l2)
    r = stack_union(l1, l2)
    print(r)
