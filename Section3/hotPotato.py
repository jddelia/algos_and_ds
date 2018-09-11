#! /usr/bin/python3

# This program uses a queue to simulate hot potato.

from queue import Queue

def hot_potato(names, constant):
    qnames = Queue()
    for i in names:
        qnames.enqueue(i)

    count = 0
    while qnames.size() > 1:
        for i in qnames.items:
            qnames.enqueue(qnames.dequeue())
            count += 1
            if count % constant == 0:
                qnames.dequeue()

    return qnames.items

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))
