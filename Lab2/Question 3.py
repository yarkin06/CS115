# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:57:44 2019

@author: yarkin.yildiz-ug
"""

""" 3)	Write a script to input  n (number of lines) and displays the output below.

1
1 2
1 2 3
..
1 2 …  n
"""

lines = float(input("Enter the number of lines: "))

if lines % 1 != 0:
    print("Please enter an integer number.")

else:
    for i in range(1,int(lines) + 1):
        for numbers in range(1,i+1):
            print(numbers,end=" ")
        print()
        