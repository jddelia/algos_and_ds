#! /usr/bin/python3

""" This program creates anagram detectors using different
    approaches with respect to time complexity. """


def anagram_detector1(word1, word2):

    for i in word2:
        if i not in word1:
            return False
    return True

def anagram_detector2(word1, word2):

    w1 = list(word1).sort()
    w2 = list(word2).sort()

    return w1 == w2

def anagram_detector3(word1, word2):

    w1 = [0] * 27
    w2 = [0] * 27

    for i in word1:
        position = ord(i) - 96
        w1[position] += 1

    for i in word2:
        position = ord(i) - 96
        w2[position] += 1

    return w1 == w2

print(anagram_detector1('god', 'dog'))
print(anagram_detector2('god', 'dog'))
print(anagram_detector3('god', 'dog'))
