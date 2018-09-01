#! /usr/bin/python3

""" This program compares the time efficiency of the 'del' function
    between lists and dictionaries using the timeit module. """

from timeit import Timer

x = list(range(2000000))
listdel = Timer("del x[1000]", "from __main__ import x")
print("List del operation: ", listdel.timeit(number=1000), "seconds.")

x = {i: None for i in range(2000000)}
dictdel = Timer("del x[1000]", "from __main__ import x")
print("Dict del operation: ", dictdel.timeit(number=1000), "seconds.")
