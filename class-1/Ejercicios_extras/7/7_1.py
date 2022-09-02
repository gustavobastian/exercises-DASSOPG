#! /usr/bin/python3
# characters

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os

tupleEl=(1,2,3,4,5,6,7,8)
tupleEl2=(1,2,4,3,5,6,7,8)
tupleEl3=('a','b','c','d','e','f','g','h')
tupleEl4=('a','b','c','e','d','f','g','h')
tupleEl5=('aa','ba','ca','da','ea','fa','ga','ha')
tupleEl6=('aa','ba','ca','ea','da','fa','ga','ha')

def isSorted(x):
    for i in range(1, len(x)):
        if x[i]<x[i-1]: return False
        else: continue
    return True

if __name__ == "__main__":
    data=1
    while data != "q":
        os.system('clear')      
        
        #caractA=(input("Number in binary:"))            
        
        print(isSorted(tupleEl))
        print(isSorted(tupleEl2))
        print(isSorted(tupleEl3))
        print(isSorted(tupleEl4))
        print(isSorted(tupleEl5))
        print(isSorted(tupleEl6))
        
        #print(convertBinary(str(caractA)))
        
        
        

        print("want to repeat?(enter q to exit)")
        data= (input(">"))