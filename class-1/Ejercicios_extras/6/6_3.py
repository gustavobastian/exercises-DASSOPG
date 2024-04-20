#! /usr/bin/python3
# characters

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os


def insert_char(string, char, max):    
    s=""
    count=0
    for i in range (0, len(string)):
        if (count<max):
            s+=string[i]+str(char)
            count+=1
        else :
            s+=string[i]   
        
    return s

def replace_char(string, char,max):    
    s=""
    count=0
    for i in range (0, len(string)):
        if (string[i] == " ")and (count<max):
             s+= str(char)
             count+=1
        else : s+=string[i]
    return s

def replace_number(string, char,max):    
    s=""
    count=0
    for i in range (0, len(string)):
        if (string[i].isdigit()==True) and (count<max): 
             s+= str(char)
             count+=1
        else : s+=string[i]
    return s


def insert3(string, char, max):    
    s=string[0]
    count=0
    for i in range (1, len(string)):
        if ((i%3==0) and (count<max)):  
            s+= str(char)+string[i]
            count+=1
        else : s+=string[i]
    return s    

data=1
while data != "q":
    os.system('clear')      
    caract=(input("character :"))            
    caractA=(input("character Array:"))            
    max=int(input("max subs:"))            
   
    print(insert_char(caractA,caract,max))
    print(replace_char(caractA,caract,max))
    print(replace_number(caractA,caract,max))
    print(insert3(caractA,caract,max))
    

    print("want to repeat?(enter q to exit)")
    data= (input(">"))
