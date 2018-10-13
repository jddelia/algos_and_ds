#! /usr/bin/python3

""" This program converts infix expressions to
    prefix expressions. """

from stack import Stack

def infixToPre(expression):
    expression = ''.join(expression.split())
    new_ex = []
    for index, item in enumerate(expression):
        if item in ['*', '/']:
            new_ex.insert(index-1, item)
            continue
        if item in ['+', '-']:
            new_ex.insert(0, item)
            continue
        new_ex.append(item)
    return ''.join(new_ex)

print(infixToPre('2+3+4*5'))
print(infixToPre('2+3+4+5'))
print(infixToPre('A*B+C*D'))
