#! /usr/bin/python3
# 
from math import pi,sqrt,pow
import os

def is_even(x):
    if(x==0): return False
    if(x%2==0): return True

def is_prime(x):
    for i in range (2,x):
        if(x%i==0): return False
    return True    


number=1
while (number!=0):
    os.system('clear')
    print("Welcome to understanding numbers")
    print("Input the number to be evaluated(0 for exit):")
    number=int(input(">"))
    if(is_even(number)==True): print("the number is Even")
    elif number!=0  : print("the number is Odd")
    else : print(" ")

    if(is_prime(number)==True): print("the number is Prime")
    elif number!=0  : print("the number is not Prime")

    n=input("press enter to continue")

