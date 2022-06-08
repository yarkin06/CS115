# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:38:41 2019

@author: yarkin.yildiz-ug
"""

from classes import *

def schedulePatients(filename,patientsList):
    file = open(filename+ ".txt","r")
    
    for line in file:
        a = line.split(";")
        if a[5] == "True":
            details = Outpatient(a[0],a[5],a[1],a[2],a[4],a[3],a[6])
        else:
            details = Outpatient(a[0],a[5],a[1],a[2],a[4],a[3],0)
        patientsList.append(details)
        
    return patientsList

patientsList = []

schedulePatients("patients",patientsList)

patientsList.sort()
    
print(patientsList)
    