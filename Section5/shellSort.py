#! /usr/bin/python3

# This program implements a shell sort.

def shell_sort(lst):
    increment = 3
    count = 0
    while count < increment:
        for i in range(count, len(lst), increment):
            position = i
            value = lst[i]

            while position > 0 and lst[position-1] > value:
                lst[position] = lst[position-1]
                position -= 1

            lst[position] = value

        count += 1

    for i in range(1, len(lst)):
        position = i
        value = lst[i]

        while position > 0 and lst[position-1] > value:
            lst[position] = lst[position-1]
            position -= 1

        lst[position] = value

def main():
    lst = [54,26,93,17,77,31,44,55,20]
    shell_sort(lst)
    print(lst)

if __name__ == "__main__":
    main()
