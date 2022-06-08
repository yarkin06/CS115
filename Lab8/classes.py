# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 08:44:48 2019

@author: yarkin.yildiz-ug
"""

import datetime

class Patient:
    
    __hospitalFee = 500
    
    def __init__(self,pName,isInsured,coveragePercent):
        self.__name = pName
        self.__insure = isInsured
        self.__percent = coveragePercent
        
    def setName(self,pName):
        self.__name = pName
    
    def setInsure(self,isInsured):
        self.__insure = isInsured
        
    def setPercent(self,coveragePercent):
        self.__percent = coveragePercent
        
    def getName(self):
        return self.__name
    
    def getInsure(self):
        return self.__insure
    
    def getPercent(self):
        return self.__percent
    
    def getValue(self):
        return self.__hospitalFee
    
    def __repr__(self):
        if self.__insure:
            return ("\nPatient Name: " + self.__name + " Insurance: (yes)")
        else:
            return ("\nPatient Name: " + self.__name + " Insurance: (no)")
    
    def calculateFee(self):
        return ((100 - int(self.__percent)) * int(self.__hospitalFee))/100
    
    

class Outpatient(Patient):
    
    def __init__(self,pName,isInsured,appointmentDate,appointmentTime,polyClinic,doctorName,coveragePercent):
        Patient.__init__(self,pName,isInsured,coveragePercent)
        self.setAppointmentDate(appointmentDate)
        self.__time = appointmentTime
        self.__clinic = polyClinic
        self.__dName = doctorName
    def getTime(self):
        return self.__time
    
    def setAppointmentDate(self,appointmentDate):
        today = datetime.datetime.strptime(appointmentDate, "%Y%m%d").date()
        self.__date = today
        
    def getDate(self):
        return self.__date
    
    def __lt__(self,other):
        
        if (self.getDate(),self.getTime()) < (other.getDate(),other.getTime()):
            return True
        else:
            return False
    
    def __repr__(self):
        if Patient.getInsure(self) == "True":

            return ("\n\nAppointment Date: " + str(self.__date) + " " + self.__time + "\nPatient Name: " + str(Patient.getName(self)) + " Insurance: (yes)" + "\nPoly Clinic: " + self.__clinic + " (" + self.__dName + ")\nFee: " + str(Patient.calculateFee(self)))
        else:
            return ("\n\nAppointment Date: " + str(self.__date) + " " + self.__time + "\nPatient Name: " + str(Patient.getName(self)) + " Insurance: (no)" + "\nPoly Clinic: " + self.__clinic + " (" + self.__dName + ")\nFee: " + str(Patient.calculateFee(self)))
    