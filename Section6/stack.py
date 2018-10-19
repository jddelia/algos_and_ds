#! /usr/bin/python3

# This program implements the stack abstrack data type.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def pop(self):
        return self.items.pop()

def revstring(string):
    stack = Stack()
    for i in string:
        stack.push(i)

    new_string = ""
    for i in range(len(stack.items)):
        new_string += stack.pop()

    return new_string

if __name__ == '__main__':

    print(revstring('doG'))

    stack = Stack()
    print(stack.is_empty())
    stack.push(4)
    stack.push('dog')
    print(stack.peek())
    stack.push(True)
    print(stack.size())
    print(stack.is_empty())
    stack.push(8.4)
    x = stack.pop()
    print(x)
    x = stack.pop()
    print(x)
    print(stack.size())
