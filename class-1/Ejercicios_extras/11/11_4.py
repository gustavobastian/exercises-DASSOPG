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


def count_words(text):
    textS=text.split(" ")
    count=0
    for word in textS:
        count+=1
    return count    

def count_char(text):
    count=0
    for i in range(0,len(text)):
        if(text[i]!=" "): count+=1
        else : continue
    return count    

def wc(filename):
    file=open(filename, 'r')
    lines = file.readlines()
    data=len(lines)
    countw=0
    countc=0
    for i in range(0,len(lines)):
        countw+=count_words(lines[i])
        countc+=count_char(lines[i])
    print(f"lines:{data}" )
    print(f"countw:{countw}" )
    print(f"countc:{countc}" )

    return 0


##testing

if __name__ == "__main__":
    
    data=1
    lista={}
    while data != "q":
        x=0
        os.system('clear')      
        a = (sys.argv[1])
        
    
        wc(a)      
        
        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))