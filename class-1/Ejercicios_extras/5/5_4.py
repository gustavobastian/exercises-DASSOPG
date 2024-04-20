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
        number_ins=int(input(">"))
        if(number_ins==0): exit(0)
        if(number_ins==number):
            print("you Win!")
            exit(0)
        else: 
            os.system('clear')
            print("not yet")
            if(number_ins>number):
                print("number is too large")
            else:    
                print("number is too small")
            time.sleep(0.5)    
