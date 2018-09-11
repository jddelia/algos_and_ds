#! /usr/bin/python3

""" This program converts infix expressions  to postfix
    expressions. Credit: Problem Solving With Algos/DS. """

from stack import Stack

def infixToPost(expression):
    expression = ''.join(expression.split())
    prec = {}
    prec['-'] = 1
    prec['+'] = 1
    prec['*'] = 1
    prec['/'] = 1
    prec['^'] = 1
    opstack = Stack()
    postfix = []
    symbols = []

    for item in expression:
        if item == ')':
            postfix.append(opstack.pop())
            continue
        if item in prec:
            opstack.push(item)
        if item.isalnum() == True:
            postfix.append(item)

    while not opstack.is_empty():
        postfix.append(opstack.pop())
    return ''.join(postfix)

print(infixToPost('((A*B)+(C*D))'))
print(infixToPost('(A+(B*(C*D)))'))
print(infixToPost('((A+B)*(C+D))'))
print(infixToPost('((A + B) * C)'))
print(infixToPost('(A + B * C)'))
print(infixToPost("(10 + ((3 * 5) / (16 - 4)))"))
print(infixToPost("(5 * (3 ^ (4 - 2)))"))
