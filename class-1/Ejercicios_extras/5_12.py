#! /usr/bin/python3
# primes numbers

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os


number_of_exercises= 10
percent= 7.0


def resolvedEx(x,number_of_exercises,percent):
    number_of_exercises= 10
    percent= 70
    if( (x/number_of_exercises)> (percent/100 ) ):
        return "approved"
    else: return "dissaproved"

data=1
number_of_exercises=int(input("ejercicios:"))        
percent=int(input("porcentaje(1...100):")) 

while data != "q":
    os.system('clear')      
    digit=int(input("ejercicios resueltos:"))        
    
    print(resolvedEx(digit,number_of_exercises,percent))

    
    

    print("want to repeat?(enter q to exit)")
    data= (input(">"))
