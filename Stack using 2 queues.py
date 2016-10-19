# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:43:36 2016

@author: Kanika Mathur
"""

class Stack:
    #initialize data structure here
    def __init__(self):
        self.q1 = []
        self.q2 = []
    
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q1.append(x)
    
    # @return nothing
    def pop(self):
        while self.q1:
            temp = self.q1.pop(0)
            if self.q1:
                self.q2.append(temp)
        self.q1 = self.q2
        self.q2 = []
    
    # @return an integer
    def top(self):
        while self.q1:
            temp = self.q1.pop(0)
            self.q2.append(temp)
        self.q1=self.q2
        self.q2=[]
        return temp
    
    # @return a boolean
    def empty(self):
        if self.q1:
            return False
        return True
        
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.top())
    