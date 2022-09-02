#! /usr/bin/python3
# working with files

from ast import literal_eval
from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
import sys
from syslog import LOG_UPTO
import time
import os



def rot13(src, dest):
    with open(src, "r") as f1:
        with open(dest, "w") as f2:            
            byte = f1.read(1)
            while (byte):
                if (byte<="z" and byte>="a" ):                    
                    byte2=ord(byte)+13                    
                    if(byte2>0x7a):
                        d=byte2-0x7a
                        byte2=d+0x61-1

                    byte=chr(byte2)
                f2.write(byte)
                byte = f1.read(1)

##testing

if __name__ == "__main__":
    
    os.system('clear')      
    a = (sys.argv[1])
    b = (sys.argv[2])
    rot13(a,b)
        
    
    
        
        
    