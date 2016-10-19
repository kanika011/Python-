# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:05:08 2016

@author: Kanika Mathur
"""


class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()
    
    def is_Empty(self):
        return self.items == []
        
    def peep(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)
        

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_Empty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.is_Empty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))
