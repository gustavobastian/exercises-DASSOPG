#! /usr/bin/python3
# primes numbers

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os

def first2(x):
    d=str(x)
    if(len( d)<2): return 0
    else:
        s=x[0]+x[1]
        return s

def last3(x):
    d=str(x)
    if(len( d)<3): return 0
    else:
        s= x[-3]+ x[-2] + x[-1]
        return s        

def char2(x):
    d=str(x)
    if(len( d)<2): return 0
    else:
        i=2
        s=d[0]
        while i < len(d):                        
            if(i%2==0): s+=d[i]
            
            i+=1
        return s        

def inverted(x):
    d=str(x)
    z=len(d)
    i=1
    s=""
    while i < len(d):                        
            s+=d[-i]            
            i+=1
    s+=d[0]                 
    return s        


data=1
while data != "q":
    os.system('clear')      
    caract=(input("character Array:"))            
   
    print(str(first2(caract)))
    print(str(last3(caract)))
    print(str(char2(caract)))
    print(str(inverted(caract)))
    print(str(caract)+str(inverted(caract)))

    print("want to repeat?(enter q to exit)")
    data= (input(">"))
