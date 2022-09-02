#! /usr/bin/python3
# functions in functions

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os


d=[1,2,4,7,5,6,3,4,3,10,11]


def findArgument(x, value):
    count=0
    for item in x:
        if(item==value): count +=1
        else: continue
    return count

def findFirstPosition(x, value):    
    for i in range(0, len(x)):
        if(x[i]==value): return i
        else: continue
    return "not Found"

def findAllPosition(x, value):
    output=[]
    for i in range(0,len(x)):
        if(x[i]==value): output.append(i)
        else: continue
    return output  



##testing

if __name__ == "__main__":
    data=1

    while data != "q":
        x=0
        os.system('clear')      
        print("original:"+str(d))
        print("looking for 3:"+str(findArgument(d,3)))
        print("First Position of 3:"+str(findFirstPosition(d,3)))
        print("looking for 200:"+str(findFirstPosition(d,200)))

        print("All positions for 3:"+str(findAllPosition(d,3)))
        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))