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
    print("s:"+str(s))
    return s   

def convert_binary(x2):
    x=x2
    sum_l=0
    xi=1
    if (x[0]=='1'): sum_l+=1
    if(len(x)==1): return sum_l
    for i in range (1,len(x)):
        sum_l*=2 
        if x[i]=='1': sum_l+=xi        
    return sum_l

if __name__ == "__main__":
    data=1
    while data != "q":
        os.system('clear')      
        
        caractA=(input("Number in binary:"))            
        
        
        print(convert_binary(str(caractA)))
        
        
        

        print("want to repeat?(enter q to exit)")
        data= (input(">"))