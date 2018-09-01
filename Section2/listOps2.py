#! /usr/bin/python3

""" This program uses the timeit module to test the time
    efficiency of the pop() function in for lists. """

from timeit import Timer

x = list(range(2000000))
endpop = Timer("x.pop()", "from __main__ import x")
print("Pop from end: ", endpop.timeit(number=1000), "seconds")

x = list(range(2000000))
midpop = Timer("x.pop(x[int(len(x)/2)])", "from __main__ import x")
print("Pop from middle: ", midpop.timeit(number=1000), "seconds")

x = list(range(2000000))
indexpop = Timer("x.pop(0)", "from __main__ import x")
print("Pop from start: ", indexpop.timeit(number=1000), "seconds")
