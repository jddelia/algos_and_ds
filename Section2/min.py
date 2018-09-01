#! /usr/bin/python3

""" This program compares two functions used to find
    the minimum value element in a list. """

import time

def minimum1(lst):

    start = time.time()
    for num in lst:
        for index, othernum in enumerate(lst):
            if num > othernum:
                break
            if index == len(lst) - 1:
                end = time.time()
                return num, (end - start)

def minimum2(lst):

    check = lst[0]
    start = time.time()
    for num in lst[1:]:
        if num < check:
            check = num
    end = time.time()

    return check, (end - start)

lst = [10,6,4,7,7,4,1,6,4,9,2]

print(minimum1(lst))
print(minimum2(lst))
