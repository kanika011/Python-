# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:40:14 2016

@author: Kanika Mathur
"""


def pascal(n):
    for line  in range(1,n+1):
        c = 1
        for i in range(1, line+1):
            print(c)
            c = c *(line-i)/i
        print(" ")
        
pascal(5)
