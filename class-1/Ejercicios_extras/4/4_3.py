#! /usr/bin/python3
# function that prints the identity matrix
from math import pi,sqrt,pow
import os
matrix=[]
line=[]
def identity(x):
    for i in range (0,x):
        line=[]
        for j in range (0,x):
            if i==j : line.append(1)
            else: line.append(0)
        print(line)    
    
