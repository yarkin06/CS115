# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:47:19 2019

@author: yarkin.yildiz-ug
"""

def findDigits(number):
    first = number // 10 ** (len(str(number))-1)
    last = number % 10
    return (first, last)

number = int(input("Enter an integer number (<=0 will stop the program): "))

while number > 0:
    first, last = findDigits(number)
    
    if first == last:
        print(str(number) + " has the same first digit and last digit")
        number = int(input("Enter an integer number (<=0 will stop the program): "))
    else:
        number = int(input("Enter an integer number (<=0 will stop the program): "))