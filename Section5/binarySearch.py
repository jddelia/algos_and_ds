#! /usr/bin/python3

# This program implements a binary search.

def binary_search1(lst, item):
    """ Testing """
    if len(lst) == 1:
        return item
    else:
        mid = len(lst) // 2
        if lst[mid] == item:
            return item
        elif lst[mid] > item:
            return binary_search1(lst[:mid], item)
        else:
            return binary_search1(lst[mid:], item)

def binary_search2(lst, item, start, end):
    mid = (start + end) // 2
    if lst[start] == item:
        return item
    else:
        if lst[mid] == item:
            return item
        elif lst[mid] > item:
            end = mid
            return binary_search2(lst, item, start, end)
        else:
            start = mid
            return binary_search2(lst, item, start, end)

def binary_search3(lst, item):
        start = 0
        end = len(lst)
        print()
        while True:
            print("start:", start)
            print("end:", end)
            mid = (start + end) // 2
            print("mid:", mid)
            print()
            if lst[mid] == item:
                return item
            elif lst[mid] > item:
                end = mid
                continue
            else:
                start = mid
                continue

def main():
    lst = list(range(1, 101))
    print(binary_search1(lst, 49))

    print(binary_search2(lst, 49, 0, 100))

    print(binary_search3(lst, 49))

if __name__ == "__main__":
    main()
