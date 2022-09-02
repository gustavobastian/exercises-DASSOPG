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



def copy(src, dest):
    with open(src, "rb") as f1:
        with open(dest, "wb") as f2:
            # Copy byte by byte
            byte = f1.read(1)
            while (byte):
                f2.write(byte)
                byte = f1.read(1)

    


##testing

if __name__ == "__main__":
    
        os.system('clear')      
        a = (sys.argv[1])
        b = (sys.argv[2])                
       # print(f"{a}")
       # print(f"{b}")
        copy(a,b)      
        
        
        print("copying done")
        