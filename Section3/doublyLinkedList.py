#! /usr/bin/python3

# This program implements a doubly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_next(self, data):
        self.next = data

    def get_next(self):
        return self.next

    def set_back(self, item):
        self.back = item

    def get_back(self, item):
        return self.back

class UnorderedList:
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

    def add(self, item):
        node = Node(item)
        node.set_next(self.root)
        if self.size == 0:
            self.root = node
            self.size += 1
            return
        else:
            self.root = node
            self.root.set_back(node)

    def search(self, item):
        current = self.root
        check = False
        while not check:
            if current.data == item:
                check = True
                return True
            else:
                current = current.get_next()
            if current == None:
                return False

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

def main():
    dub = UnorderedList()
    dub.add(10)
    print(dub)
    dub.add(30)
    dub.add(20)
    print(dub)

if __name__ == "__main__":
    main()
