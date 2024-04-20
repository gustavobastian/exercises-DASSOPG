#! /usr/bin/python3
# characters

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os


def inverted(x):
    d=str(x)    
    i=1
    s=""
    while i < len(d):                        
            s+=d[-i]            
            i+=1
    s+=d[0]                 
    return s   

def insert3(string, char):    
    s=string[0]
    for i in range (1, len(string)):
        if (i%3==0):
              s+= str(char)+string[i]           
        else : s+=string[i]
    return s    


def printing_miles(x):
    s=inverted(x)
    print(s)    
    s2=insert3(s,'.')
    print(s2)
    output=inverted(s2)
    print(output)
    

data=1
while data != "q":
    os.system('clear')      
    
    caractA=(input("character Array:"))            
    
   
    printing_miles(str(caractA))
    
    

    print("want to repeat?(enter q to exit)")
    data= (input(">"))
