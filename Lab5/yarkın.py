# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:50:09 2019

@author: yarkin.yildiz-ug
"""

file = open("CS115.txt","r")
d = {1:[],2:[],3:[]}

for line in file:
    words = line.split(";")
    
    if words[1] == str(1):
        a = (words[0],int(words[2]))
        d[1].append(a)
    
    elif words[1] == str(2):
        b = (words[0],int(words[2]))
        d[2].append(b)
    
    elif words[1] == str(3):
        c = (words[0],int(words[2]))
        d[3].append(c)

def sectionAverages(d):
    
    averagelist = []
    total1 = 0
    total2= 0
    total3 = 0
    count1=0
    count2=0
    count3 = 0
    for i in d:
        for value in d[i]:
            if i == 1:
                
                total1 += value[1]
                count1 += 1


            elif i == 2:
                total2 += value[1]
                count2 += 1
                

                
            elif i == 3:
                total3 += value[1]
                count3 += 1

    average1 = total1/count1
    averagelist.append(average1)
            
    average2 = total2/count2
    averagelist.append(average2)
            
    average3 = total3/count3
    averagelist.append(average3)

    return averagelist

def changeSection(d,num,new):
    
    for i in d:
        for value in d[i]:
            if num not in value[0]:
                print("Student ",num," does not exist")
                return False
            elif i == str(new):
                print("Student ",num," already in that section")
                return False
            else:
                d[i].remove(value)
                a = value
                d[new].append(a)
                print("Student has been moved")
                return True
            break
            
def maxGrade(d):
    
    maximum = 0
    
    for i in d:
        for k in range(1,len(d)):
            if d[i][k][1] > maximum:
                maximum = d[i][k][1]
                studentId = d[i][k][0]
    
    return studentId,maximum

def printDictionary(d):
    
    for i in d:
        print("Section: ",i,"\n")
        for value in d[i]:
                print(value,"\n")
            
printDictionary(d)
averages = sectionAverages(d)
print("Section averages:",averages)
changeSection(d,"21641234",2)
changeSection(d,"22141734",3)
changeSection(d,"21112222",3)
printDictionary(d)
maximumGrade = maxGrade(d)
print("Student with highest grade: ",maximumGrade)