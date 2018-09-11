#! /usr/bin/python3

""" This program uses the Dequeue abstract data structure
    to create a palindrome checker. """

from dequeue import Dequeue

def isPalindrome(string):
    dequeue_string = Dequeue()
    for i in string:
        dequeue_string.addFront(i)

    for i in dequeue_string.items:
        if dequeue_string.removeFront() != dequeue_string.removeRear():
            return False
    return True

print(isPalindrome('radar'))
