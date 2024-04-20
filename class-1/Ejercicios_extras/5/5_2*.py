#! /usr/bin/python3
# Prime numbers factoring
from math import pi,sqrt,pow
import os


def is_prime(x):
    for i in range (2,x):
        if(x%i==0): return False
    return True    

def prime(x):    
    return x



data=1
while data!= "0":
    os.system("clear")
    data=input(">")
    print(str(prime(int(data))))
    if(data=="0"): exit(0)
    print("presione enter to continue( enter q to exit):")
    if(input(">")=="q"): exit(0)




