#! /usr/bin/python3

# This program implements an ordered list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_next(self, data):
        self.next = data

    def get_next(self):
        return self.next

class OrderedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        current = self.root
        check = False
        while not check:
            if current == None:
                return ""
                break
            print("[", current.data, "]", end="")
            current = current.get_next()

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def search(self, item):
        current = self.root
        for i in range(self.size):
            if current.data > item:
                return False
            if current.data == item:
                return True
            current = current.get_next()
        return False

    def add(self, item):
        node = Node(item)
        current = self.root
        previous = self.root
        check = False
        while not check:
            if current == None:
                if self.root == None:
                    self.root = node
                    self.size += 1
                    check = True
                    return
                previous.set_next(node)
                self.size += 1
                check = True
                return
            if current.data > item:
                previous.set_next(node)
                node.set_next(current)
                self.size += 1
                check = True
                return
            previous = current
            current = current.get_next()

myList = OrderedList()
myList.add(10)
print(myList.size)
myList.add(15)
myList.add(10)
myList.add(20)
print(myList)
print(myList.size)
