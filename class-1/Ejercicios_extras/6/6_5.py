#! /usr/bin/python3
# characters

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os

def first_l(x):
    data=x.split(' ')
    output=""
    for i in range(0,len(data)):
        output+=data[i][0]
    return output

def first_m(x):
    data=x.split(' ')
    output=""
    for i in range(0,len(data)):
        output+=(data[i][0]).upper()
        for j in range (1,len(data[i])):
            output+=data[i][j]
        output+=" "
    return output

def words_a(x):
    data=x.split(' ')
    output=""
    for i in range(0,len(data)):
        if (((data[i][0])=='A') or ((data[i][0])=='a')):
            for j in range (0,len(data[i])):
                output+=data[i][j]
            output+=" "
    return output

data=1
while data != "q":
    os.system('clear')      
    
    caractA=(input("character Array:"))            
    
   
    print(first_l(str(caractA)))
    print(first_m(str(caractA)))
    print(words_a(str(caractA)))
    
    

    print("want to repeat?(enter q to exit)")
    data= (input(">"))
