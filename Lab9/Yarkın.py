# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:50:34 2019

@author: yarkin.yildiz-ug
"""

from doctor import *

def bubbleSort (data):
    issorted = False
    j = 0
    while(j < len(data)-1 and not issorted):
        issorted = True
        for k in range(len(data)-j-1):
                 
                if data[k].getHospital() > data[k+1].getHospital():
                    issorted = False
                    temp = data[k]
                    data[k] = data[k+1]
                    data[k+1] = temp
                
                elif data[k].getHospital() == data[k+1].getHospital():
                    if data[k].getSpecialty() > data[k+1].getSpecialty():
                        issorted = False
                        temp = data[k]
                        data[k] = data[k+1]
                        data[k+1] = temp
        j = j + 1
        
def binarySearch(data, Id, startInd, endInd):
    
    if(startInd > endInd):
        return -1
    
    else:
        mid = (startInd + endInd)//2
        if str(data[mid].getDoctorId()) == str(Id):
            return mid
        
        elif str(data[mid].getDoctorId()) > str(Id):
            return binarySearch(data, Id, startInd, mid-1)
        
        else:
            return binarySearch(data, Id, mid+1, endInd)
        
def readDoctors(l, filename):
    file = open(filename,"r")
    for line in file:
        x = line.split(";")
        doctor = Doctor(x[0], x[1], x[2], x[3])
        l.append(doctor)
        
doctorList = []
readDoctors(doctorList, "doctors.txt")

doctorList.sort()

Id = input("Enter id of doctor to search: ")

if binarySearch(doctorList, Id, 0, len(doctorList)) == -1:
    print("No such doctor.")
else:
    print("Doctor with id "+Id)
    print(doctorList[(binarySearch(doctorList, Id, 0, len(doctorList)))])

print("Doctors by Hospital and Specialty:")
    
bubbleSort(doctorList)
for el in doctorList:
    print(el,end="")