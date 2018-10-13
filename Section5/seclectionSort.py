#! /usr/bin/python3

# This program implements a selection sort.

import math

def selection_sort(lst):
    new_lst = []
    lowest = math.inf

    for passnum in range(len(lst)):
        for i in lst:
            if i in new_lst:
                if new_lst.count(i) == lst.count(i):
                    continue
            if i < lowest:
                lowest = i
        new_lst.append(lowest)
        lowest = math.inf
    return new_lst

def main():
    lst = [26,54,93,17,77,31,44,55,20]

    print(selection_sort(lst))

if __name__ == "__main__":
    main()
