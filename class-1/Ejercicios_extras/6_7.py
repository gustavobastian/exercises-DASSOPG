#! /usr/bin/python3
# characters

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os

def isSubs(carA, carS):
    d=len(carA)-len(carS)
    print(d)
    for i in range(0, len(carA)-len(carS)+1):
        print(carA[i:i+len(carS)])
        if(carA[i:i+len(carS)]==carS) : return True
        else :continue
    return False

def comparison(carA,carS):
    if(carA>carS): return carS
    else : return carA


data=1
while data != "q":
    os.system('clear')      
    
    caractA=(input("character sustring:"))            
    caractAA=(input("character Array:"))            
    
    print(comparison(str(caractAA),str(caractA)))
    #print(isSubs(str(caractAA),str(caractA)))
    
    

    print("want to repeat?(enter q to exit)")
    data= (input(">"))