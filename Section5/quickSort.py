#! /usr/bin/python3

# This program implements a quick sort.

def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)

def quick_sort_helper(lst, first, last):
    if first < last:
        split = split_finder(lst, first, last)

        quick_sort_helper(lst, 0, split - 1)
        quick_sort_helper(lst, split + 1, last)

def split_finder(lst, first, last):
    pivot = lst[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        print(lst)
        while lst[left_mark] < pivot:
            left_mark += 1
        while lst[right_mark] > pivot:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            left = lst[left_mark]
            lst[left_mark] = lst[right_mark]
            lst[right_mark] = left
            left_mark += 1
            right_mark -= 1
    lst[first] = lst[right_mark]
    lst[right_mark] = pivot

    return right_mark

def main():
    lst = [54,26,93,17,77,31,44,55,20]
    quick_sort(lst)
    print(lst)

if __name__ == "__main__":
    main()
