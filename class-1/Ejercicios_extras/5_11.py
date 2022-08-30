#! /usr/bin/python3
# primes numbers

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os



def digitN(x1,y2):
    if ((x1>10) and (y2<10)): 
        x= y2
        y= x1
    elif ((y2>10) and (x1<10)): 
        y= y2
        x= x1
    else: 
        print("error")    
        return False

    data=str(y)

    for i in range(0,len(data)):
        if(data[i]==str(x)): return True

    return False



data=1
while data != "q":
    os.system('clear')      
    digit=int(input("insert digit:"))        
    number1=int(input("insert number1:"))       

    print(digitN(digit,number1))
    

    print("want to repeat?(enter q to exit)")
    data= (input(">"))
