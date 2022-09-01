#! /usr/bin/python3
# characters

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os


def convertStr2Tup(str):
    x=str.split(',')
    if((len(x)!=2)): 
        print("Error")
        return(0,0)
    elif (((int(x[0]))<0) or((int(x[0]))>9)) :
        print("Error")
        return (0,0)
    elif (((int(x[1]))<0) or((int(x[1]))>9)) :
        print("Error")
        return (0,0)    
    else:
        return int(x[0]),int(x[1]) 

def convertStr2Tup2(str):
    x=str.split('-')
    if((len(x)!=2)): 
        print("Error")
        return(0,0)
    elif (((int(x[0]))<0) or((int(x[0]))>9)) :
        print("Error")
        return (0,0)
    elif (((int(x[1]))<0) or((int(x[1]))>9)) :
        print("Error")
        return (0,0)    
    else:
        return int(x[0]),int(x[1]) 

def canUse(x,y):    
    if((x[0])== (y[0]) or((x[0])==(y[2])) ):         
        return True
    if((x[2])==(y[0]) ) or((x[2])==(y[2])):         
        return True
    else :return False

if __name__ == "__main__":
    data=1
    while data != "q":
        os.system('clear')      
        
        primerFicha=str(input("First token (ej 1,2):"))            
        segundaFicha=str(input("Second token (ej 1,2):"))            
        
        print(convertStr2Tup2(primerFicha))
        print(convertStr2Tup2(segundaFicha))
        

        print(canUse(primerFicha,segundaFicha))
        
        
        #print(convertBinary(str(caractA)))
        
        
        

        print("want to repeat?(enter q to exit)")
        data= (input(">"))