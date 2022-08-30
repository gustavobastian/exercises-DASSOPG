#! /usr/bin/python3
# characters

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os

x=("Pedro Vivas","Rosario","Alberto ", "Santo Domingo","Estefania Sl","Unilater Ac")
xx=(("Pedro Vivas","M"),("Rosario","F"),("Alberto ","M"),("Estefania L","F"),("Santo Domingo ","M"))

def printE(x):
    for i in range(0, len(x)):
        print("Estimado "+str(x[i])+",vote por mi")

def printEBis(x):
    for i in range(0, len(x)):
        print("Estimado "+str(x[i][0])+",vote por mi")


def printE2(x,origen, cant):
    if((origen<0) or (cant<0)):
        print("Error")
        return
    if ((len(x))>(origen+cant)):
        d=origen+cant
    else:
        d=len(x)    
    if(origen>1)    :
        ori =origen-1
    else:
        ori= 0    

    for i in range(ori, d):
        print("Estimado "+str(x[i])+",vote por mi")

def printE2Bis(x,origen, cant):
    if((origen<0) or (cant<0)):
        print("Error")
        return
    if ((len(x))>(origen+cant)):
        d=origen+cant
    else:
        d=len(x)    
    if(origen>1)    :
        ori =origen-1
    else:
        ori= 0    

    for i in range(ori, d):
        if(str(x[i][1])=="M"):
            print("Estimado "+str(x[i][0])+",vote por mi")
        else: 
            print("Estimada "+str(x[i][0])+",vote por mi")    


data=1
while data != "q":
    os.system('clear')      
    
   # primerFicha=str(input("First token (ej 1,2):"))            
   # segundaFicha=str(input("Second token (ej 1,2):"))            
    
   # print(convertStr2Tup2(primerFicha))
   # print(convertStr2Tup2(segundaFicha))

   # print(canUse(primerFicha,segundaFicha))
    
    
    #print(convertBinary(str(caractA)))
    printE(x)
    print("********************************")
    printE2(x,3,2)
    print("********************************")
    printEBis(xx)
    print("********************************")
    printE2Bis(xx,3,2)
    print("********************************")

    print("want to repeat?(enter q to exit)")
    data= (input(">"))