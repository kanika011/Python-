# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:06:12 2016

@author: Kanika Mathur
"""

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def printQueue(self):
        count = 0
        while count < len(self.items):
            print(self.items[count])
            count += 1
        

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items)-1]

def interLeaveQueue(q):
    if q.size() % 2 != 0:
        return
    s = Stack()
    halfSize = q.size()/2
    for i in range(0, halfSize):
        s.push(q.dequeue())
    while not s.isEmpty():
        q.enqueue(s.pop())
    for i in range(0, halfSize):
        s.push(q.dequeue())
    while not s.isEmpty():
        q.enqueue(s.pop())
        q.enqueue(q.dequeue())
    q.printQueue()

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
q.enqueue(80)
q.printQueue()
interLeaveQueue(q)
        