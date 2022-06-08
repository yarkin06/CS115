# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:22:53 2019

@author: yarkin.yildiz-ug
"""

import numpy as np
from matplotlib.pyplot import *
from math import *

seeds = np.loadtxt("seed.txt")

weeks = np.arange(1,16)

clf()
subplot(2,1,1)
plot(weeks,seeds,"bo-")
title("Order 1")
subplot(2,1,2)
plot(weeks,seeds,"bo")
title("Order 2")
legend(["seeds"])