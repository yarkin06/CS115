# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:51:32 2019

@author: yarkin.yildiz-ug
"""

class MenuItem:
    
    def __init__(self,itemName,itemDescription,ingredients,itemCalories,itemCost):
        self.__name = itemName
        self.__description = itemDescription
        self.__ingredients = ingredients
        self.__calories = itemCalories
        self.__cost = itemCost
    
    def setCalories(self,itemCalories):
        self.__calories = itemCalories
        
    def setCost(self,itemCost):
        self.__cost = itemCost
        
    def setName(self,itemName):
        self.__name = itemName
        
    def setDescription(self,itemDescription):
        self.__description = itemDescription
        
    def setIngredients(self,ingredients):
        self.__ingredients = ingredients
        
            
    def getName(self):
        return self.__name
    
    def getCalories(self):
        return self.__calories
    
    def getCost(self):
        return self.__cost
    
    def getDescription(self):
        return self.__description
    
    def getIngredients(self):
        return self.__ingredients
    
    def __repr__(self):
        return ("\nMenu item  [itemDescription = "+ self.__description+ ", itemName = "+ self.__name+", calories = "+ self.__calories+ ", ingredients = "+ self.__ingredients+ ", itemCost = "+ self.__cost)
    
    def getAverageCostPerIngredient(self):
        return float(self.getCost())/int(self.getIngredients())
        
