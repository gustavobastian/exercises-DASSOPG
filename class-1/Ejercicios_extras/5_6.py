#! /usr/bin/python3
# guessing numbers

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os

def isPowerOfTwo(x):
    d=1    
    while(d<=x):
      #  print("d:"+str(d))
        n=2
        for i in range (1,d):
            n*=2
     #   print("n:"+str(n))    
        if(n==x):return True
        elif (n<x): d+=1
        else : return False

def numberSum(x1,x2):
    sum=0
    for i in range (x1,x2+1):
        if(isPowerOfTwo(i)):
            sum+=i
    return sum        


number=0
data=1
while data != "0":
    os.system('clear')      
    number1=int(input("insert number1:"))        
    number2=int(input("insert number2:"))        
    print("suma:"+str(numberSum(number1,number2)))

    print("want to repeat?(0 exits)")
    data= (input(">"))
