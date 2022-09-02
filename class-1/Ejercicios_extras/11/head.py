#! /usr/bin/python3
# working with files

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
import sys
from syslog import LOG_UPTO
import time
import os


def printingN(filename,n):
    file=open(filename, 'r')
    lines = file.readlines()
    d=len(lines)
    if(d>n): d=n   
    

    for i in range(0,d):
        print(f"{lines[i]}")


##testing

if __name__ == "__main__":
    
    lista={}
    
    
    os.system('clear')      
    a = (sys.argv[1])
    b = int(sys.argv[2])                
       # print(f"{a}")
       # print(f"{b}")
    printingN(a,b)      
        
        
        