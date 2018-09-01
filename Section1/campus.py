#! /usr/bin/python3

""" This program creates a class heirarchy for
    people on a college campus. """

from random import choice

class Person:

    id = 1

    def __init__(self, first, last, title):
        self.first = first
        self.last = last
        self.title = title.capitalize()
        self.id = Person.id
        Person.id += 1

class Roster:

    def __init__(self, name):
        self.name = name
        self.roster = {'Faculty':[], 'Staff': [], 'Students':[]}

    def populate(self, lst):
        for i in lst:
            self.roster[i.title].append((i.id, i.last, i.first, i.title))

first = ['John', 'Sarah', 'Chelsea', 'Chad', 'Jessica']
last = ['Thompson', 'Brown', 'Jean', 'Watson', 'Smith']
title = ['Students', 'Faculty', 'Staff']

ros = []

for i in range(20):
    person = Person(choice(first), choice(last), choice(title))
    ros.append(person)

roster1 = Roster('MIT')
roster1.populate(ros)

print('\n' + roster1.name + ':\n')
for i in roster1.roster.values():
    print(i)
