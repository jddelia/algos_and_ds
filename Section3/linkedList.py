#! /usr/bin/python3

# This program is an implementation of the linked list abstract data type.

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
        self.root = node
        self.size += 1

    def remove(self, item):
        current = self.root
        check = False
        previous = None
        while not check:
            if current.data == item:
                self.size -= 1
                if current == self.root:
                    self.root = self.root.get_next()
                    check = True
                    continue
                previous.set_next(current.get_next())
                check = True
            else:
                previous = current
                current = current.get_next()
            if current == None:
                raise Exception("Value Error: Item not in list")

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

    def append(self, item):
        node = Node(item)
        current = self.root
        for i in range(self.size):
            if i == self.size - 1:
                self.size += 1
                current.set_next(node)
                break
            current = current.get_next()

    def index(self, item):
        current = self.root
        for i in range(self.size):
            if current.data == item:
                return i
            current = current.get_next()

    def insert(self, pos, item):
        node = Node(item)
        current = self.root
        if pos == 0:
            self.add(item)
            return
        if pos >= self.size:
            self.append(item)
        for i in range(self.size):
            if i == pos:
                previous.set_next(node)
                node = previous.get_next()
                node.set_next(current)
                self.size += 1
                return
            previous = current
            current = current.get_next()

    def pop(self, pos=None):
        current = self.root
        for i in range(self.size):
            if i == pos:
                item = current.data
                self.remove(current.data)
                return item
            if i == self.size - 2:
                item = current.get_next().data
                current.set_next(None)
                self.size -= 1
                return item
            current = current.get_next()

class OrderedList(UnorderedList):
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


def main():
    unlist = UnorderedList()
    print(unlist.is_empty())
    unlist.add(10)
    unlist.add(20)
    unlist.add(30)
    unlist.add(40)
    print(unlist)
    print(unlist.get_size())
    unlist.remove(20)
    print(unlist.get_size())
    print(unlist)
    print(unlist.search(10))
    print(unlist.is_empty())
    unlist.remove(40)
    print(unlist.get_size())
    unlist.append(40)
    unlist.append(20)
    print(unlist)
    print(unlist.index(10))
    unlist.insert(1, 20)
    print(unlist)
    print(unlist.pop())
    print(unlist)
    unlist.append(20)
    print(unlist)
    print(unlist.pop(3))
    print(unlist)

    myList = OrderedList()
    myList.add(10)
    print(myList.size)
    myList.add(15)
    myList.add(10)
    myList.add(20)
    print(myList)
    print(myList.size)

if __name__ == "__main__":
    main()
