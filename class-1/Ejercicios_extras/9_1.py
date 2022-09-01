#! /usr/bin/python3
# functions in functions

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os

##testing

if __name__ == "__main__":
    data=1
    while data != "q":
        x=0
        os.system('clear')      
        
        d=int(input("Ingrese nro: "))
        
        print(str(find(lista,d)))
        
        #print(str(lista))
        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))