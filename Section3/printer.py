#! /usr/bin/python3

""" This program simulates a printer and its scheduling
    operations, within certain parameters. """

import random
from queue import Queue

def printing(tasks, page_time):
    printer = Queue()
    wait_times = []

    for i in range(1, tasks + 1):
        new_task = random.randint(1, 180)
        pages = random.randint(1, 20)
        print_time = pages * page_time
        printer.enqueue((new_task, print_time))

    print(printer.items)

    count = 0
    while count < (tasks - 1):
        if count == 0:
            wait = (printer.items[count][1] - printer.items[count + 1][0])
            if wait < 0:
                wait_times.append((0, printer.items[count + 1][1]))
            else:
                wait_times.append((wait, wait + printer.items[count + 1][1]))
            count += 1
            continue
        wait = (wait_times[count - 1][1] - printer.items[count + 1][0])
        if wait < 0:
            wait_times.append((0, printer.items[count + 1][1]))
        else:
            wait_times.append((wait, wait + printer.items[count + 1][1]))

        count += 1

    print(wait_times)

    total = 0
    for i in wait_times:
        total += i[0]
    print(total/len(wait_times))


printing(20, 6)
