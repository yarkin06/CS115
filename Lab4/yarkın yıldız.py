# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:57:17 2019

@author: yarkin.yildiz-ug
"""

from Q1_module import *


file = "input"

ChoiceUser = displayMenu()

while ChoiceUser != "c":

    if ChoiceUser == "a":
    
        domain = input("Enter domain to search: ")
        findEmailByDomain(domain,file)
        print(findEmailByDomain(domain,file), " users exit in ",domain, " domain")
        ChoiceUser = displayMenu()
    
    elif ChoiceUser == "b":
    
        domain_2 = input("Enter domain to search: ")
        displayUsersHavingNumeric(domain_2)
        break
        
if ChoiceUser == "c":
    print("Goodbye!")