#! /usr/bin/python3
# functions in functions

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os


lista=[(1,"Lavandina ayudin",2.1),(2,"Alcohol Ethilico",10),(3,"Pan comun",2.9),(4,"Pan Integral",3.4),(6, "Alfajor Jorgito",5),(7, "Aceituna verde",2)]

element=3



#binary search

def find(lista,value):
    
    if ((len(lista)==1) and (value!=lista[0][0])):                
        return "No se encontró"
    
    d=int(len(lista)/2)
    
    if(value==lista[d][0]):return lista[d]
    elif (value>lista[d][0]): 
        x=slice(d,len(lista))
        return find(lista[x],value)
    else : 
        x=slice(d)
        return find(lista[x],value)
    





##testing

if __name__ == "__main__":
    data=1
    while data != "q":
        x=0
        os.system('clear')      
        
        d=int(input("Ingrese nro: "))
        
        print(str(find(lista,d)))
        
        #print(str(lista))
        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))