# -*- coding: utf-8 -*-
"""
Created on Mon May 13 08:47:13 2019

@author: yarkin.yildiz-ug
"""

from matplotlib.pyplot import *

import numpy as np

from math import *

x = np.arange(-pi,pi + 0.01,0.01)

y1 = pi/2
y2 = pi/2
y3 = pi/2

for i in range(1,5,2):
    y1 += 2*(np.sin(i*x)/i)
    
for i in range(1,9,2):
    y2 += 2*(np.sin(i*x)/i)
    
for i in range(1,27,2):
    y3 += 2*(np.sin(i*x)/i)

    

clf()    
plot(x,y1,"r")
plot(x,y2,"b")
plot(x,y3,"g")
legend(["n = 2","n = 4","n = 13"])