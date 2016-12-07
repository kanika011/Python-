# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:21:57 2016

@author: Kanika Mathur
"""

# Implementing a queue

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
        return 0
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

q=Queue()
q.enqueue(4)
q.enqueue('dog')
print(q.size())