#! /usr/bin/python3.7

# This program implements a binary heap.

class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size += 1
        parent = self.heap_list[self.current_size // 2]
        i = self.current_size
        while i // 2 > 0:
            if self.heap_list[i] < parent:
                temp = parent
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = parent
                i //= 2
                parent = self.heap_list[i // 2]
            else:
                break

    def del_min(self):
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list.pop()
        self.current_size -= 1
        i = 1
        while i * 2 < self.current_size:
            if self.heap_list[i] > self.heap_list[i * 2]:
                temp = self.heap_list[i * 2]
                self.heap_list[i * 2] = self.heap_list[i]
                self.heap_list[i] = temp
                i *= 2
            try:
                if self.heap_list[i] > self.heap_list[(i * 2) + 1]:
                    temp = self.heap_list[(i * 2) + 1]
                    self.heap_list[(i * 2) + 1] = self.heap_list[i]
                    self.heap_list[i] = temp
                    i *= 2
                else:
                    break
            except:
                self.heap_list.append(self.heap_list[i])
        return min_val

    def build_heap(self, lst):
        lst.sort()
        self.heap_list.append(lst[0])
        for i in lst:
            self.insert(i)
