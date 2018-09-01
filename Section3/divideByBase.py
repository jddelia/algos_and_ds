#! /usr/bin/python3

# This program implements the 'divide by 2' algorithm.

from stack import Stack

def base_to_base(num, base):
    digits = "0123456789ABCDEF"
    num_stack = Stack()
    while num > 0:
        num, rem = divmod(num, base)
        num_stack.push(rem)

    num_string = ""
    while not num_stack.is_empty():
        num_string += digits[num_stack.pop()]

    return num_string

print(base_to_base(256, 16))
