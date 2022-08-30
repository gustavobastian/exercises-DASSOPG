#! /usr/bin/python3
# guessing numbers

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os

number=0
sum=0
prom=0
index=0
while number != -1:
    os.system('clear')      
    index+=1
    print("Insert Number "+str(index)+" (-1 for exit):")
    number=int(input(">"))        
    sum+=number
    prom=sum/index
    
print("Numbers inserted:", index)
print("Sum:"+str(sum))
prom2=round(prom,2)
print("Prom:"+str(prom2))
exit(0)

    
    
