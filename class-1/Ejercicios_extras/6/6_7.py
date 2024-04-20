#! /usr/bin/python3
# characters

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os

def is_subs(car_a, car_s):
    d=len(car_a)-len(car_s)
    print(d)
    for i in range(0, len(car_a)-len(car_s)+1):
        print(car_a[i:i+len(car_s)])
        if(car_a[i:i+len(car_s)]==car_s) : return True
        else :continue
    return False

def comparison(car_a,car_s):
    if(car_a>car_s): return car_s
    else : return car_a

if __name__ == "__main__":
    data=1
    while data != "q":
        os.system('clear')      
        
        caractA=(input("character sustring:"))            
        caractAA=(input("character Array:"))            
        
        print(comparison(str(caractAA),str(caractA)))
        #print(isSubs(str(caractAA),str(caractA)))
        
        print("want to repeat?(enter q to exit)")
        data= (input(">"))