#! /usr/bin/python3

# This program checks to see that parentheses are balanced.

from stack import Stack

def is_balanced(string):
    stack = Stack()
    balanced = True
    index = 0

    while balanced and index < len(string):
        if string[index] in '({[':
            stack.push(string[index])
        else:
            if stack.is_empty():
                balanced = False
                break
            else:
                if string[index] == is_match(stack.items[-1]):
                    stack.pop()
                else:
                    balanced = False
                    break

        index += 1

    if balanced and stack.is_empty():
        return True
    else:
        return False

def is_match(string):
    if string == '(':
        return ')'
    if string == '{':
        return '}'
    if string == '[':
        return ']'


print(is_balanced("((()))"))
print(is_balanced("((())))"))
print(is_balanced("(((){}})))"))
print(is_balanced("(((){}()))"))
