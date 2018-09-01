from timeit import Timer

def divideBy2(num):
    num_lst = []
    while num > 0:
        num, rem = divmod(num, 2)
    return num_lst

x = 0
t1 = Timer("divideBy2(x)", "from __main__ import divideBy2, x")
print(t1.timeit(number=1000))
