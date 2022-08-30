#! /usr/bin/python3
# primes numbers

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os


def isPrime(x):
    for i in range (2,x):
        if(x%i==0): return False
    return True    

def primes(x):
    i=1
    while i<x:
        i+=1
        if(isPrime(i)== True): print(i)

data=1
while data != "q":
    os.system('clear')      
    number1=int(input("insert number1:"))        

    primes(number1)
    

    print("want to repeat?(enter q to exit)")
    data= (input(">"))
