#! /usr/bin/python3.7

# This program implements a Binary Search Tree.

class BinarySearchTree:
    def __init(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(Self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root == None:
            node = TreeNode(key, val)
        else:
            self._put(key, val, self.root)
        self.size += 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = Tree(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = Tree(key, val, parent=current_node)

    def __setitem__(self, key, val):
        self.put(key, val)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.payload
            else:
                return None
        else:
            return None


    def _get(self, key, current_node):
        if key == current_node.key:
            return current_node.payload
        elif key < current_node.key:
            if current_node.has_left_child():
                self._get(key, current_node.left_child)
            else:
                return None
        else:
            if current_node.has_right_child():
                self._get(key, current_node.right_child)
            else:
                return None

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node = self._get(key, self.root)
            if node:
                self.remove(node)
                self.size -= 1
        elif self.root.key == key and self.size == 1:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not in tree")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, node):
        if node.has_both_children():
            node.left_child.parent = node.parent
            node.right_child.parent = node.left_child
            node.left_child.right_child = node.right_child

            if not node.parent:
                successor = node.find_successor()
                if successor:
                    self.remove(successor)
                node.key = successor.key
                node.payload = successor.payload

                if successor.has_right_child():
                    if successor != node.right_child:
                        successor.right_child.parent = successor.parent
                        if successor.right_child.key < successor.parent
                            successor.parent.left_child = successor.right_child
                        else:
                            successor.parent.right_child = successor.right_child

            if node == node.parent.left_child:
                node.parent.left_child = node.left_child
            elif node == node.parent.right_child:
                node.parent.right_child = node.left_child

        elif node.has_any_children():
            if node.has_left_child():
                node.left_child.parent = node.parent

                if not node.parent:
                    node.replace_node_data(node.left_child.key,
                                            node.left_child.payload,
                                            node.left_child.left_child,
                                            node.left_child.right_child)
                    return

                if node == node.parent.left_child:
                    node.parent.left_child = node.left_child
                elif node == node.parent.right_child:
                    node.parent.right_child = node.left_child
            else:
                node.right_child.parent = node.parent

                if not node.parent:
                    node.replace_node_data(node.right_child.key,
                                            node.right_child.payload,
                                            node.right_child.left_child,
                                            node.right_child.right_child)
                    return

                if node == node.parent.left_child:
                    node.parent.left_child = node.right_child
                elif node == node.parent.right_child:
                    node.parent.right_child = node.right_child
        else:
            if node == node.parent.left_child:
                node.parent.left_child = None
            elif node == node.parent.right_child:
                node.parent.right_child = None

    def __iter__(self):
        if self:
            if self.has_left_child():
                for item in self.left_child:
                    yield item
            yield self.key
            if self.has_right_child()
                for item in self.right_child:
                    yield item

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_min(self):
        current = self
        while current.has_left_child:
            current = current.left_child
        return current

    def find_successor(self):
        successor = None
        if self.has_right_child():
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor
