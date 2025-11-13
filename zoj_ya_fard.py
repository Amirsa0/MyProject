#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 20:38:01 2025

@author: amirsa
"""

def is_even (number) :
    if number % 2 == 0 :
        return True
    else : 
        return False


number = int(input())    
print(is_even(number))    