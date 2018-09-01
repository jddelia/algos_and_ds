#! /usr/bin/python3

""" This program tests different ways to build a list of numbers,
    and uses the timeit module to measure time efficiency. """

from timeit import Timer

def test1():
    lst = []
    for i in range(1000):
        lst = lst + [i]

def test2():
    lst = []
    for i in range(1000):
        lst.append(i)

def test3():
    lst = [i for i in range(1000)]

def test4():
    lst = list(range(1000))

def test5():
    return

t = Timer("test5()", "from __main__ import test5")
t = t.timeit(number=1000)

t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000) - t, "seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000) - t, "seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000) - t, "seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000) - t, "seconds")
