# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:29:53 2018

@author: HNAF
"""

Wii=65
money=input("Masukkan nilai uang yg dipunya: ")
money=int(money)
print ("Uangmu yaitu",str(money))

if money<Wii:
    print("Kamu butuh",str(Wii-money),"untuk membeli Wii")
else:
    print("Kamu dapat",str(money/Wii),"dan kembali",str(money-Wii))