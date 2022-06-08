# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:49:01 2019

@author: yarkin.yildiz-ug
"""
""" 1)	Write a program to input the age of 10 people and print out the number of people whose ages are above 50 years old and the average age of the people who are below 20 years old. You should not store the ages in a list.
"""

AgeTotalBelow20 = 0
NumberOfBelow20 = 0
NumberOfAbove50 = 0
NumberOfPeople = 1
MaxPeople = 10

for ages in range(1,MaxPeople + 1):
    
    age = float(input("Enter the age of person " + str(NumberOfPeople) + ": "))

    if age < 20:
        AgeTotalBelow20 += age
        NumberOfBelow20 += 1
    
    elif age > 50:
        NumberOfAbove50 += 1
        
    NumberOfPeople += 1

if NumberOfBelow20 == 0:
    print("You didn't enter any age below 20. ")

else:
    AverageOfBelow20 = AgeTotalBelow20 / NumberOfBelow20
    print("Average age of people whose ages are below 20: " + str(AverageOfBelow20))
    
print("There are " + str(NumberOfAbove50) + " people whose ages are above 50.")