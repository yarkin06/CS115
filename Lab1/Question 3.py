# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 09:04:07 2019

@author: yarkin.yildiz-ug
"""

""" Question 3
"""
budget = float(input("Please write your budget in TL: "))
if budget < 0:
    print("Please write a positive number!")
elif budget < 15:
    print("More money needed.")
elif budget < 23:
    print(("Main dish added. Budget is not sufficient for the desert and the starter. Total meal cost: 15TL. Remaining budget = ") + str(budget - 15) + ("TL"))
elif budget < 25:
    print(("Main dish added. Budget is not sufficient for starter. Desert added. Total meal cost : 23TL. Remaining budget = ") + str(budget - 23) + ("TL"))
elif budget < 33:
    print(("Main dish added. Budget is sufficient only for starter or desert. Starter added firstly. Since starter added first, budget is not sufficient for the desert. Total meal cost: 25TL. Remaining budget = ") + str(budget - 25) + ("TL"))
else:
    print(("Main dish added. Budget is sufficient for both starter and desert. Starter added. Desert added. Total meal cost: 33TL. Remaining budget = ") + str(budget - 33) + ("TL"))
    