#! /usr/bin/python3

# This program implements the dequeue abstract data structure.

class Dequeue:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeRear(self):
        return self.items.pop(0)

    def removeFront(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    d = Dequeue()
    print(d.items)
    print(d.is_empty())
    print(d.items)
    d.addRear(4)
    print(d.items)
    d.addRear("dog")
    print(d.items)
    d.addFront("cat")
    print(d.items)
    d.addFront(True)
    print(d.items)
    print(d.size())
    print(d.items)
    print(d.is_empty())
    print(d.items)
    d.addRear(8.4)
    print(d.items)
    print(d.removeRear())
    print(d.items)
    print(d.removeFront())
    print(d.items)
