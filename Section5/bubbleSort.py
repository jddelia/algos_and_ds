#! /usr/bin/python3

# This program implements a bubble sort.

def bubble_sort(lst):
    length = len(lst)
    new_lst = []
    higher = lst[0]
    changed = True
    index = 0

    while changed:
        if index == length - 1:
            print(new_lst)
            new_lst.append(higher)
            if new_lst == lst:
                changed = False
                return new_lst
            else:
                lst = new_lst
                new_lst = []
                index = 0
                higher = lst[0]
                continue
        if higher < lst[index+1]:
            new_lst.append(higher)
            higher = lst[index+1]
        else:
            new_lst.append(lst[index+1])
        index += 1

def main():
    lst = [2,1,3,5,4]
    print(bubble_sort(lst))

if __name__ == "__main__":
    main()
