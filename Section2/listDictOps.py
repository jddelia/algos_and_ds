#! /usr/bin/python3

""" This program tests the time efficiency of the in function
    between dictionaries and lists. """

from timeit import Timer

x = list(range(2000000))
inlist = Timer("100000 in x", "from __main__ import x")
print("In for list: ", inlist.timeit(number=1000), "seconds.")

x = {}
for i in range(2000000):
    x[i] = 1
indict = Timer("1000000 in x", "from __main__ import x")
print("In for dict: ", indict.timeit(number=1000), "seconds.")
