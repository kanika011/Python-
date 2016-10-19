# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:34:56 2016

@author: Kanika Mathur
"""

class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()
    
    def is_empty(self):
        return self.items == []
        
    def peep(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)
        

def par_checker(symbol_string):
    s=Stack()
    balanced=True
    index=0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top= s.pop()
                if not matches(top, symbol):
                    balanced = False
        index+=1
    if balanced and s.is_empty():
        return True
    else:
        return False
        
def matches(open, close):
    opens="([{"
    closes=")]}"
    return opens.index(open) == closes.index(close)
    
print(par_checker('{{([])()}'))
print(par_checker('[{()]'))