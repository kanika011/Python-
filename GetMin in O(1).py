# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 19:58:39 2016

@author: Kanika Mathur
"""

class Stack:
    def __init__(self):
        self.items = []
        self.item1 = []
    def push(self, item):
        if self.item1 != []:
            data = self.item1[len(self.item1)-1]        
            if item < data:        
                self.item1.append(item)        
        else:
            self.item1.append(item)
        self.items.append(item)
        
    def pop(self):
        if self.item1 != []:
            if self.item1[len(self.item1)-1] == self.items[len(self.items)-1]:
                self.item1.pop()                 
        self.items.pop()
        
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]
    def getmin(self):
        return self.item1[len(self.item1)-1]

s = Stack()
s.push(10)
s.push(20)
print(s.peek())
print(s.getmin())
s.push(2)
print(s.getmin())