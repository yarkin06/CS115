# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:32:31 2018

@author: b
"""

class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, d, loc):
        self.drunks[d] = loc
        
    def getDrunks(self):
       return self.drunks
   
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            print('Drunk not in field')
        else:
            xDist, yDist = drunk.takeStep()
            currentLocation = self.drunks[drunk]
            #use move method of Location to get new location
            self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            print('Drunk not in field')
        else:
            return self.drunks[drunk]