#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 20:29:38 2025

@author: amirsa
"""

def sum_of_squares (number1,number2):
    sum_of_square = (number1**2) + (number2**2)
    return sum_of_square

number1=int(input())
number2=int(input()) 

print(sum_of_squares(number1, number2))   