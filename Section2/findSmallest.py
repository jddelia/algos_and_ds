#! /usr/bin/python3

""" This program find the smallest kth element in a list
    in O(n), and O(nlog n) time. """

from timeit import Timer

def find_smallest1(lst, kth):
    lst.sort()
    return lst[kth-1]

def find_smallest2(lst, kth):
    x = 0
    for i in lst:
        if i < x:
            x = i

x = list(range(2000))

t1 = Timer("find_smallest1(x, 10)", "from __main__ import x, find_smallest1")
print("Time to run find_smallest1: ", t1.timeit(number=1000), "seconds.")
