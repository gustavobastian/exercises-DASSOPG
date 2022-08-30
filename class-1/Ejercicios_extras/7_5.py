#! /usr/bin/python3
# 2D vectors

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
import time
import os

list=[1,2,3,4,5,6,7]
#list=[1,1,1,1,1,1,1]



tableFactorial = [1,1]

def factorial(x):
    if x<0: return print("error debe ser >0")
    elif x<len(tableFactorial) : return tableFactorial[x]    
    elif x==(len(tableFactorial)) : 
        tableFactorial.append(x*tableFactorial[x-1])
        print(tableFactorial)
        return tableFactorial[x]
    else :
        for i in range (2,x+1):
            tableFactorial.append(i*tableFactorial[i-1])
        return tableFactorial[x]    
    


def isPrime(x):
    for i in range (2,x):
        if(x%i==0): return False
    return True   

def listPrime(x):
    out=[]
    for i in range (0,len(x)):
        if(isPrime(x[i])==True):
            out.append(x[i])
    return out        


def listFactorial(x):
    out=[]
    for i in range (0,len(x)):
        out.append(factorial(x[i]))
    return out        



def sumProm(x):
    sum=0
    prom=0
    count=0
    for i in range (0,len(x)):
        sum+=x[i]
        count+=1
    prom=sum/count    
    return sum,prom    



data=1
while data != "q":
    os.system('clear')      
    print((list))
    print(listPrime(list))
    var=sumProm(list)
    print("prom:"+str(var[1])+"|sum:"+str(var[0]))
    print(listFactorial(list))

    print("want to repeat?(enter q to exit)")
    data= (input(">"))