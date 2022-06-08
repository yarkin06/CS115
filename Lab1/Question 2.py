# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 08:55:24 2019

@author: yarkin.yildiz-ug
"""

""" Question 2
"""
number = float(input("Please write an integer number: "))
if number % 1 != 0:
    print("It is not an integer number!")
elif number < 0:
    print("Number is not positive.")
elif number > 0 and number % 2 == 0:
    print("Number is even and positive.")
elif number > 0 and number % 2 != 0:
    print("Number is odd and positive.")
else:
    print("Number is equal to zero.")