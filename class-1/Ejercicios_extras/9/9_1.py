#! /usr/bin/python3
# functions in functions

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os
lista = [('Hola','don Pepito'),('Hola','don Jose'),('Buenos ','dias')]

def tuplas_a_diccionario(x):
    mydic={}
    print(len(x))
    for i in range(0,len(x)):
        
        if(mydic.get(x[i][0])==None): 
            #print(" not found")
            mydic.update({str(x[i][0]):[str(x[i][1])]})
        else:
            #print("found")
            aux=mydic.get(x[i][0])
            aux.append(x[i][1])
            mydic.update({str(x[i][0]):aux})
         #print(str(x[i][0])+":"+str(x[i][1]))
    return mydic 


##testing

if __name__ == "__main__":



    data=1
    while data != "q":
        x=0
        os.system('clear')      
        
        print(tuplas_a_diccionario(lista))
        
        #print(str(lista))
        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))