# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:39:17 2016

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

def consecutiveIntegers(s):
    q = Queue()
    pairwiseOrdered= 1
    while  not s.isEmpty():
        q.enqueue(s.pop())
    while not s.isEmpty():
        s.push(q.dequeue())
    while not s.isEmpty():
        n = s.pop()
        q.enqueue(n)
        if not s.isEmpty():
            m = s.pop()
            q.enqueue(m)
            if abs(n-m) != 1:
                pairwiseOrdered = 0
    while not s.isEmpty():
        s.push(q.dequeue())
    return pairwiseOrdered

s=Stack()
s.push(4)
s.push(5)
s.push(-2)
s.push(-3)
s.push(11)
s.push(10)
s.push(5)
s.push(6)
s.push(20)
print(consecutiveIntegers(s))
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
