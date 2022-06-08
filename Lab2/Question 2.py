# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:57:44 2019

@author: yarkin.yildiz-ug
"""

""" 2)	Write a program to input a positive integer from the user. The program should display whether or not the digits of the number are in descending order (left to right).  Note: the number may have any number of digits.
"""

number = input("Enter a positive integer: ")
TrueCount = 0

if float(number) < 0:
    print("Your number should be positive.")
    
elif float(number) % 1 != 0:
    print("Your number should be an integer.")

else:
    for i in range(1,len(number)):
        if number[i-1] > number[i]:
            TrueCount += 1
    
    if TrueCount == 0:
        print("Your number's length is one, it can't be assessed whether it is in descending order or not.")

    elif TrueCount == len(number) - 1:
        print("Digits are in descending order.")

    else:
        print("Digits are not in descending order.")
            