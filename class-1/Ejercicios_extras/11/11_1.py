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


##testing

def printingN(filename,n):
    file=open(filename, 'r')
    lines = file.readlines()
    d=len(lines)
    if(d>n): d=n   
    

    for i in range(0,d):
        print(f"line {i+1} : {lines[i]}")


if __name__ == "__main__":
    text= "este es un texto que posee muchas palabras extraordinariamente largas , y es bonito"
    data=1
    lista={}
    while data != "q":
        x=0
        os.system('clear')      
        a = (sys.argv[1])
        b = int(sys.argv[2])                
       # print(f"{a}")
       # print(f"{b}")
        printingN(a,b)      
        
        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))