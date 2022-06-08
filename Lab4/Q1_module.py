# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:44:24 2019

@author: yarkin.yildiz-ug
"""

def displayMenu():
    print("Menu: ")
    print("(a) Find email by domain")
    print("(b) Display numeric userNames by domain")
    print("(c) EXIT")
    
    choice = input("Enter choice: ")
    
    while choice != "a" and choice != "b" and choice != "c":
        
        print("Menu: ")
        print("(a) Find email by domain")
        print("(b) Display numeric userNames by domain")
        print("(c) EXIT")
    
        choice = input("Enter choice: ")
    
    return choice
        
def findEmailByDomain(domain,inputfile):
    
    b = inputfile+ ".txt"
    file = open(b, "r")
    
    outfile = open(domain+ ".txt", "w")
    
    num = 0
    for line in file:
        pos_1 = line.find("@")
        pos_2 = line.find(".")
        
        if line[pos_1 + 1:pos_2] == domain:
            
            outfile.write(line[:pos_1]+ "\n")
            num += 1
            
    outfile.close()
    
    return num
            
def displayUsersHavingNumeric(domain):
    
    try:
        a = domain+ ".txt"
        file = open(a, "r")
        file = open("input.txt", "r")
        for line in file:
            for i in ("0123456789"):
                if line.find(i) != -1:
                    pos_1 = line.find("@")
                    pos_2 = line.find(".")
                    print(line[:pos_1]+ "\n")
                    break
        file.close()
        
    except:
        print("No such file exists")