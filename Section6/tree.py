#! /usr/bin/python3

# This program implements a tree abstract data type through
# the list of lists method.

myTree = ['a', #root
    ['b', #left subtree
    ['d', [], []], #child
    ['e', [], []], #child
    ],
    ['c', #right subtree
    ['f', [], []]
    ] #child
]

def binary_tree(root):
    return [root, [], []]

def insert_left(root, new_branch):
    left_subtree = root.pop(1)
    if len(left_subtree) > 1:
        root.insert(1, [new_branch, left_subtree, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    right_subtree = root.pop(2)
    if len(right_subtree) > 1:
        root.insert(2, [new_branch, [], right_subtree])
    else:
        root.insert(2, [new_branch, [], []])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, val):
    root[0] = val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def main():
    newTree = binary_tree(1)
    insert_left(newTree, 2)
    insert_left(newTree, 3)
    insert_right(newTree, 4)
    insert_right(newTree, 5)
    print(newTree)

    left_child = get_left_child(newTree)
    set_root_val(left_child, 6)
    print(newTree)

    insert_left(left_child, 7)
    print(newTree)
    print(get_right_child(get_right_child(newTree)))

def build_tree():
    newTree = binary_tree('a')
    insert_left(newTree, 'b')
    insert_right(get_left_child(newTree), 'd')
    insert_right(newTree, 'c')
    insert_left(get_right_child(newTree), 'e')
    insert_right(get_right_child(newTree), 'f')
    print(newTree)

if __name__ == '__main__':
    main()
    build_tree()
