#! /usr/bin/python3
# guessing numbers

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os

numberdiscovered=False
number=random.randrange(1,100)

while numberdiscovered==False:
        os.system('clear')        
        print("Insert number:")
        numberIns=int(input(">"))
        if(numberIns==0): exit(0)
        if(numberIns==number):
            print("you Win!")
            exit(0)
        else: 
            os.system('clear')
            print("not yet")
            if(numberIns>number):
                print("number is too large")
            else:    
                print("number is too small")
            time.sleep(0.5)    
