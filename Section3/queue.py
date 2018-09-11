#! /usr/bin/python3

# This program implements the 'Queue' abstract data type.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self, index=-1):
        return self.items.pop(index)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

if __name__ == "__main__":

    queue = Queue()
    
    print(queue.is_empty())
    print(queue.enqueue(4))
    print(queue.enqueue('dog'))
    print(queue.enqueue(True))
    print(queue.size())
    print(queue.is_empty())
    print(queue.enqueue(8.4))
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.size())
