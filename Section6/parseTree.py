#! /usr/bin/python3.7

# This program implements a parse tree algorithm.

import operator

from nodeTree import BinaryTree
from stack import Stack


def parse_tree(expression):
    tree = BinaryTree(0)
    current_node = tree
    parents = Stack()
    parents.push(current_node)

    for item in expression:
        if item == '(':
            current_node.insert_left(0)
            parents.push(current_node)
            current_node = current_node.get_left_child()
        elif item in ['+','-','/','*']:
            current_node.set_root_val(item)
            current_node.insert_right(0)
            parents.push(current_node)
            current_node = current_node.get_right_child()
        elif item.isdigit():
            current_node.set_root_val(int(item))
            current_node = parents.pop()
        elif item == ")":
            current_node = parents.pop()
        else:
            raise ValueError

    return tree

def parse_tree_eval(tree):
    operations = {'+': operator.add, '-': operator.sub,
                    '*': operator.mul, '/': operator.truediv}

    left_child = tree.get_left_child()
    right_child = tree.get_right_child()

    if tree.get_left_child() == None\
    and tree.get_right_child() == None:
        return tree.key
    else:
        operand = operations[tree.key]
        return operand(parse_tree_eval(left_child), parse_tree_eval(right_child))

def postorder_eval(tree):
    operations = {'+': operator.add, '-': operator.sub,
                    '*': operator.mul, '/': operator.truediv}

    res1 = None
    res2 = None
    if tree:
        res1 = postorder_eval(tree.get_left_child())
        res2 = postorder_eval(tree.get_right_child())
        if res1 and res2:
            return operations[tree.get_root_val()](res1, res2)
        else:
            return tree.get_root_val()

def print_exp(tree):
    exp = ""
    if tree:
        exp = '(' + print_exp(tree.get_left_child())
        exp += str(tree.get_root_val())
        exp += print_exp(tree.get_right_child()) + ')'
    return exp

new_exp = parse_tree(['(', '3', '+', '(', '4', '*', '5' ,')',')'])
print(new_exp)
print(parse_tree_eval(new_exp))
print(postorder_eval(new_exp))
print(print_exp(new_exp))
