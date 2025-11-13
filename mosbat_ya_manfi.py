#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 20:26:28 2025

@author: amirsa
"""

def is_positive (number) :
    if number >= 0 : 
        return True
    else :
        return False

number = int(input())
print(is_positive(number))    