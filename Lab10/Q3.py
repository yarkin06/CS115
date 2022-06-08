# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:39:17 2019

@author: yarkin.yildiz-ug
"""

import random
from Drunk import *

class EastWestDrunk(Drunk): 
    def takeStep(self):
        stepChoices = [(1,0),(-1,0)]
        return random.choice(stepChoices)
