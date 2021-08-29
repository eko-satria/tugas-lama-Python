# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:08:56 2018

@author: HNAF
"""

bil=input("Masukkan Angka: ")
bil=int(bil)

def factors(bil):
    a=0
    print("Faktor dari ",bil,"adalah: ")
    for n in range(1, bil+1):
        if bil%n==0:
            print(n)
            a=a+1
        print("Banyak faktor"+str(a))
        print(factors(bil))