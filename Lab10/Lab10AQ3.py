# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:11:52 2018

@author: b
"""
from matplotlib.pyplot import *
from Field import *
from Drunk import *
from Location import *
from Q3 import *

def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
       Moves d numSteps times, and returns the distance between
       the final location and the location at the start of the 
       walk."""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

#random.seed(0)
clf()

f = Field()

#Create 5 EastWestDrunks and add them to the field.

for i in range(1,6):
    origin = Location(0, 0)
    f.addDrunk(EastWestDrunk( "Joe"+str(i)), origin)



distances = []
drunks = f.getDrunks()
colors = ["ro", "mo", "bo", "go", "ko"]
c_Pos = 0


#Each drunk should take 10 walks of 100 steps.  
#You should plot the location of each drunk, at the end of each walk.

for i in drunks:
    for j in range(10):
        f.addDrunk(i, origin)
        distances.append(walk(f, i,100))
        plot([f.getLoc(i).getX()],[f.getLoc(i).getY()], colors[c_Pos])
        xlabel("distance")
    c_Pos += 1 




#For all walks of all drunks you should store the distance between the 
#origin and the final location, and display the average, 
#minimum and maximum distances.
    
mean = sum(distances)/len(distances)
minDist = min(distances)
maxDist = max(distances)
print("Average Distance:"+str(mean))
print("Max Distance:"+str(maxDist))
print("Min Distance:"+str(minDist))