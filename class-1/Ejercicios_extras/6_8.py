#! /usr/bin/python3
# characters

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os




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

def convertBinary(x2):
    x=inverted(x2)
    sum=0
    xi=2
    if (x[0]=='1'): sum+=2
    if(len(x)==1): return sum
    for i in range (1,len(x)):
        if x[i]=='1': sum+=xi
        xi*2 

    return sum

if __name__ == "__main__":
    data=1
    while data != "q":
        os.system('clear')      
        
        caractA=(input("Number in binary:"))            
        
        
        print(convertBinary(str(caractA)))
        
        
        

        print("want to repeat?(enter q to exit)")
        data= (input(">"))