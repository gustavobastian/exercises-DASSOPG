#! /usr/bin/python3
# primes numbers

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os


def inserChar(string, char):    
    s=""
    for i in range (0, len(string)):
        s+=string[i]+str(char)
    return s

def replaceChar(string, char):    
    s=""
    for i in range (0, len(string)):
        if (string[i] == " "): s+= str(char)
        else : s+=string[i]
    return s

def replaceNumber(string, char):    
    s=""
    for i in range (0, len(string)):
        if (string[i].isdigit()==True):  s+= str(char)
        else : s+=string[i]
    return s


def insert3(string, char):    
    s=string[0]
    for i in range (1, len(string)):
        if (i%3==0):  s+= str(char)+string[i]
        else : s+=string[i]
    return s    

data=1
while data != "q":
    os.system('clear')      
    caract=(input("character :"))            
    caractA=(input("character Array:"))            
   
    print(inserChar(caractA,caract))
    print(replaceChar(caractA,caract))
    print(replaceNumber(caractA,caract))
    print(insert3(caractA,caract))
    

    print("want to repeat?(enter q to exit)")
    data= (input(">"))
