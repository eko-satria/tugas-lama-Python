# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:32:36 2018

@author: HNAF
"""

beer=input("Berapa banyak botol: ")
beer=int(beer)
for beer in range(beer, 0, -1):
    print(str(beer), "Bottle(s) of beer on the wall,",str(beer),"Bottle(s) of beer")
    print("Take one down and pass it around",str(beer-1), "Bottle(s) of beer on the wall")
print("Exit")