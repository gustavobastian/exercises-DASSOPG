#! /usr/bin/python3
# functions in functions

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os

"""
Input variables
"""
lista=[(1,"Lavandina ayudin",2.1),(2,"Alcohol Ethilico",10),(3,"Pan comun",2.9),(4,"Pan Integral",3.4),(5, "Alfajor Jorgito",5),(6, "Aceituna verde",2)]

listaF=[(1,2),(3,5)]

"""
FUNCTIONS
"""

def find(list,value):
    output=[]
    for i in range(0,len(list)):
        if(list[i][0]==value): return(list[i])
        else: continue    
    


def printTicket(ticket,priceList):
    d=()
    total=0
    subtotal=0
    strLocal="itemId -  description  - Quantity x unitPrice = Subtotal "
    print(strLocal)    

    for i in ticket:
        subtotal=0
        d=find(priceList,i[0])
        subtotal=d[2]*i[1]
        total+=subtotal
        #print(str(d[0])+"-"+str(d[1])+"-"+str(i[1])+"-"+str(subtotal) )
        print(f"{d[0]}-{d[1]}            {i[1]}x{d[2]} ={subtotal}$")
    print("*********************************************")    
    print("TOTAL: "+str(total)+"$")    



"""
testing
"""

if __name__ == "__main__":

    data=1
    while data != "q":
        x=0
        os.system('clear')      
        
        
        print("Printing ticket:")
        
        printTicket(listaF,lista)
        
        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))