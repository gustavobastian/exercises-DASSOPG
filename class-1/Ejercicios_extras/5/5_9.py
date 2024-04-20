#! /usr/bin/python3
# multiples of a number

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os


def multiples_numbers(x1,x2):
    if(x1==1) or (x2==1): return 0
    if(x1==x2): return 1
    if x1>x2: 
        n1=x2
        n2=x1
    else:
        n1=x1
        n2=x2

    for i in range(1,n2+1):        
        if i*n1>=n2:
            return i

def multiples_numbers_w(x1,x2):
    if(x1==1) or (x2==1): return 0
    if(x1==x2): return 1
    if x1>x2: 
        n1=x2 
        n2=x1
    else:
        n1=x1
        n2=x2
    i=1
    while  i*n1<n2:
        i+=1
    return i

number=0
data=1
while data != "q":
    os.system('clear')      
    number1=int(input("insert number1:"))        
    number2=int(input("insert number2:"))        
    print("Multiples:"+str(int(multiples_numbers(number1,number2))))
    print("MultiplesW:"+str(int(multiples_numbers_w(number1,number2))))

    print("want to repeat?(enter q to exit)")
    data= (input(">"))
