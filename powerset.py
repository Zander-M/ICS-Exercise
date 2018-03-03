# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:46:06 2015

@author: zhengzhang
"""
import time
import matplotlib.pyplot as plt

# timing the execution of a function
def timeit(f, *args):
    t1 = time.time()
    f(*args)
    t2 = time.time()
    return t2 - t1


from copy import deepcopy

def powerset_rec(l):
    if not l:
        return [ [] ]
    return powerset_rec( l[1:] ) + [ [l[0] ] + x for x in powerset_rec( l[1:] ) ]

def powerset_add(l):
    pset = [[]]
    for item in l:
        new_subset = deepcopy(pset)
        print(pset)
        for subset in new_subset:
            subset.append(item)
        print(new_subset)
        pset.extend(new_subset)
        print(pset)
    return pset

def powerset_comb_list_comprehension(l):
    pset = []
    total_items = len(l)
    for i in range(2 ** total_items):
        code = bin(i).split('b')[-1]
        code = code[::-1]
        subset = [l[j] for j in range(len(code)) if code[j] == '1']
        pset.append(subset)
    return pset

def powerset_comb(l):
    pset = []
    total_items = len(l)
    for i in range(2 ** total_items):
        subset = []
        code = bin(i).split('b')[-1]
        code = code[::-1]
        for j in range(len(code)):
            if code[j] == '1':
                subset.append(l[j])
        pset.append(subset)
    return pset

def main():

    num_items = 4
    my_list = list(range(num_items))
    print(my_list)

# test using inductive logic
    my_pset = powerset_add(my_list)
    print("using induction:\n", my_pset)

# test using combinational logic
    my_pset = powerset_comb(my_list)
    print("using combination:\n", my_pset)

    exec_time = []

    for i in range(5):
        my_list = list(range(i + 1))
        takes = timeit(powerset_comb, my_list)
        exec_time.append(takes)

    print("powerset", exec_time)
# once you are done with powerset function, uncomment the line below
# and plot the execution time
    plt.plot(exec_time)
    plt.show()

main()
