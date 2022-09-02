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


def find(filename,expression):
   
    #opening filename
    file_object=open(filename,'r')    
    lines=file_object.readlines()
    
    output=[]
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])-len(expression)+1):
            #print(f"line: {i}")
            #print(lines[i][j:j+len(expression)])
            if(expression==lines[i][j:j+len(expression)]): 
                #print("TRUE")
                output.append(lines[i])
            else:    continue
            
    for i in range (0, len(output)):
        print(output[i])
    return 0

##testing

if __name__ == "__main__":
    
    os.system('clear')      
    a = (sys.argv[1])
    expression = (sys.argv[2])
    find(a,expression)
        
    
    
        
        
    