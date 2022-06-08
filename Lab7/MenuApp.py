# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:11:30 2019

@author: yarkin.yildiz-ug
"""

from MenuItemClass import *

def readMenuItems(filename):
    file = open(filename +".txt","r")
    MenuList = []

    for line in file:
        a = line.split(";")
        Menu = MenuItem(a[0],a[1],a[2],a[3],a[4])
        MenuList.append(Menu)
    return MenuList

print("Menu items:")
Menu = readMenuItems("items")

for el in Menu:
    print(el)

print("\nAll Menu Items with calories less than 1000 containing meat:")

for el in Menu:
    if "meat" in str(el):
        if int(el.getCalories()) < 1000:
            print(el)
total = 0
for el in Menu:
    average_per_el = el.getAverageCostPerIngredient()
    total += average_per_el

average = total/5
print("Average Cost Per Ingredient of All Menu Items: {:.2f}".format(average))