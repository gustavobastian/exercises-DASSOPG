#! /usr/bin/python3
# functions in functions

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os


d=[1,2,3,4,5,6,7,8,9,10,11]

def fun1(x):    
    return x+1


def fun2(x):    
    if(x>5): return True
    else: return False

def map(x, fun):
    output=[]
    for item in x:
        output.append(fun(item))
    return output


def filter(x, fun):
    output=[]
    for item in x:
        if(fun2(item))==True:
            output.append(item)
        else:
            continue    
    return output



##testing

if __name__ == "__main__":
        data=1

        while data != "q":
            x=0
            os.system('clear')      
            print("original:"+str(d))
            print("mapped:"+str(map(d,fun1)))

            print("original:"+str(d))
            print("filtered >5:"+str(filter(d,fun2)))
            
            print("\n want to repeat?(enter q to exit)")
            data= (input(">"))