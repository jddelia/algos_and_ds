#! /usr/bin/python3.7

# This program implements the preorder, inorder, and postorder
# tree traversals.

from nodeTree import BinaryTree

def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

def inorder(tree):
    if tree != None:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())

new_tree = BinaryTree("a")
new_tree.insert_left("b")
new_tree.insert_right("c")
new_tree.get_left_child().insert_right("d")
new_tree.get_right_child().insert_left("e")
new_tree.get_right_child().insert_right("f")
print(new_tree)

#new_tree.preorder()

preorder(new_tree)
print()
postorder(new_tree)
print()
inorder(new_tree)
