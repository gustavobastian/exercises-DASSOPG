#! /usr/bin/python3
# counting dictionaries

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os


def insertNumber():
    print("ingrese numero:")
    x=int(input(">"))
    return x

def findUser(user,lista):
    if(lista.get(user)==None):
            tel=insertNumber()             
            lista.update({str(user):tel})
    else:
            print(f"User:{user} | tel: {lista.get(user)}")                        
            #output.update({str(sum):aux})


##testing

if __name__ == "__main__":
    
    data=1
    lista={}
    while data != "q":
        x=0
        os.system('clear')      
        
        print("Ingresar Nombre:")
        value=input(">")
        if(value=="*"): 
            print("saliendo")
            exit(0)
        findUser(value,lista)
        
    
        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))