#! /usr/bin/python3

# This program calculates the value of a postfix expression.

from stack import Stack

import operator

def postfix_eval(expression):
    expression = expression.split()
    ops = {"+": operator.add, "-": operator.sub,
        "*": operator.mul, "/": operator.truediv}
    opstack = Stack()
    for i in expression:
        if i in "/-":
            operands = [opstack.pop(), opstack.pop()]
            opstack.push(ops[i](operands.pop(), operands.pop()))
            continue
        if i in ops:
            opstack.push(ops[i](opstack.pop(), opstack.pop()))
            continue
        opstack.push(int(i))
    return opstack.pop()

print(postfix_eval("4 5 6 * +"))
print(postfix_eval("7 8 + 3 2 + /"))
print(postfix_eval("17 10 + 3 * 9 /"))
