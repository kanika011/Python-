# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 19:12:24 2016

@author: Kanika Mathur
"""

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
        
def postFixEvaluation(symbolString):
    s= Stack()
    tokenlst=symbolString.split()
    for token in tokenlst:
        if token in '0123456789':
            s.push(int(token))
        else:
            t1=s.pop()
            t2 = s.pop()
            print(t1)
            print(t2)
            if token == '+':
                    data = t1 + t2
            
            elif token == '-':
                    data = t1 - t2
                
            elif token == '/':
                    data = t1/t2
                    
            elif token == '*':
                    data = t1 * t2
                    
            s.push(data)
            
    return s.peek()
   
print(postFixEvaluation('1 2 3 * + 5 -'))    
    
                
            
        