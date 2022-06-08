# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:47:18 2019

@author: yarkin.yildiz-ug
"""

def divisible(M,N):
    if M % N == 0:
        return True
    else:
        return False

number1 = int(input("Enter first positive integer in pair(a number <=0 will stop the program): "))
number2 = int(input("Enter second positive integer in pair(a number <=0 will stop the program): "))
NumberOfTrues = 0
NumberOfPairs = 0

while number1 > 0 and number2 > 0:
    solve = divisible(number1,number2)
    
    if solve:
        NumberOfTrues += 1
        NumberOfPairs += 1
        number1 = int(input("Enter first positive integer in pair(a number <=0 will stop the program): "))
        number2 = int(input("Enter second positive integer in pair(a number <=0 will stop the program): "))
    
    else:
        NumberOfPairs += 1
        number1 = int(input("Enter first positive integer in pair(a number <=0 will stop the program): "))
        number2 = int(input("Enter second positive integer in pair(a number <=0 will stop the program): "))
        
if NumberOfPairs == 0:
    print("You did not enter any both positive pairs.")
    
else:
    percentage = (NumberOfTrues / NumberOfPairs)*100
    print(str(percentage) + "% of the pairs are divisible by each other.")