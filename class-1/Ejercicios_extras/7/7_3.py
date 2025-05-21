#! /usr/bin/python3
# characters

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os

POINTS="********************************"
VOTE = ", vote por mi."
ESTIMADO= "Estimado, "
ESTIMADA= "Estimada, "

x=("Pedro Vivas","Rosario","Alberto ", "Santo Domingo","Estefania Sl","Unilater Ac")
xx=(("Pedro Vivas","M"),("Rosario","F"),("Alberto ","M"),("Estefania L","F"),("Santo Domingo ","M"))

def printE(x):
    for i in range(0, len(x)):
        print(ESTIMADO+str(x[i])+VOTE)

def printEBis(x):
    for i in range(0, len(x)):
        print(ESTIMADO+str(x[i][0])+VOTE)


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
        print(ESTIMADO+str(x[i])+VOTE)

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
            print(ESTIMADO+str(x[i][0])+VOTE)
        else: 
            print(ESTIMADA+str(x[i][0])+VOTE)    

if __name__ == "__main__":
    data=1
    while data != "q":
        os.system('clear')      
  
        printE(x)
        print(POINTS)
        printE2(x,3,2)
        print(POINTS)
        printEBis(xx)
        print(POINTS)
        printE2Bis(xx,3,2)
        print(POINTS)

        print("want to repeat?(enter q to exit)")
        data= (input(">"))