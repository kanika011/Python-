# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 23:35:53 2016

@author: Kanika Mathur
"""

def pallindrome(symbol):
    #symbol=symbol.casefold()
    rev_str = reversed(symbol)
    if list(symbol) == list(rev_str):
        print("It is pallindrome")
    else:
        print("It is not a pallindrome")
        
pallindrome("Enter")
pallindrome("ada")