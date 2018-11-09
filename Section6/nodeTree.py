#! /usr/bin/python3.7

# This program implements a tree data structure using
# Nodes and References.

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        structure = f"""self.key = {self.key}
        self.left_child = {self.left_child}. Key: {self.key}
        self.right_child = {self.right_child}. Key: {self.key} """
        return structure

    def insert_left(self, node):
        if self.left_child == None:
            self.left_child = BinaryTree(node)
        else:
            new_node = BinaryTree(node)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, node):
        if self.right_child == None:
            self.right_child = BinaryTree(node)
        else:
            new_node = BinaryTree(node)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def preorder(self):
        print(self.key)
        if self.get_left_child():
            self.get_left_child().preorder()
        if self.get_right_child():
            self.get_right_child().preorder()

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, val):
        self.key = val

    def get_root_val(self):
        return self.key

def main():
    new_tree = BinaryTree("a")
    new_tree.insert_left("b")
    new_tree.insert_right("c")
    new_tree.get_left_child().insert_right("d")
    new_tree.get_right_child().insert_left("e")
    new_tree.get_right_child().insert_right("f")
    print(new_tree)

if __name__ == '__main__':
    main()
