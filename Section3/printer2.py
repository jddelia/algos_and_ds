#! /usr/bin/python3

""" This program takes guidance from the book Problem Solving With Algos/DS
    Chapter 3. It simulates the scheduling/wait times of a printer. """

from random import randint
from queue import Queue

class Printer:
    def __init__(self, ppm):
        self.pageRate = 60/ppm
        self.currentTask = None
        self.time_remaining = 0

    def tick(self):
        if self.currentTask != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.time_remaining = newtask.pages * self.pageRate

class Task:
    def __init__(self, timing):
        self.pages = randint(1, 20)
        self.timestamp = timing

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def simulation(seconds, pagesPerMinute):
    printer = Printer(pagesPerMinute)
    printQueue = Queue()
    waitTimes = []

    for currentSecond in range(seconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not printer.busy()) and (not printQueue.is_empty()):
            nextTask = printQueue.dequeue()
            waitTimes.append(nextTask.waitTime(currentSecond))
            printer.startNext(nextTask)

        printer.tick()

    avgWait = sum(waitTimes) / len(waitTimes)
    return avgWait

def newPrintTask():
    num = randint(1, 180)
    if num == 180:
        return  True
    else:
        return False

for i in range(10):
    print(simulation(3600, 5))
