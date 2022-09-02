#! /usr/bin/python3
# functions in functions

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os


lista=[("Gomes,Pedro",123123),("Gamis,Jorge",53452345),("Alvarez, Done",9999999),("Filosa, Juliana",12311233),("Albertengo, Jorge",13213213)]


##from ex 6.7
def isSubs(carA, carS):
    d=len(carA)-len(carS)    
    for i in range(0, len(carA)-len(carS)+1):     
        if(carA[i:i+len(carS)]==carS) : return True
        else :continue
    return False


def find(list,value):
    output=[]
    for i in range(0,len(list)):
        if(isSubs(list[i][0],value)): output.append(list[i])
        else: continue
    
    return output


##testing

if __name__ == "__main__":
    
        data=1    

        while data != "q":
            x=0
            os.system('clear')      
            print("Ingrese parte del nombre")
            value=input(">")


            
            print("looking for i:"+str(find(lista,value)))
            
            
            
            
            print("\n want to repeat?(enter q to exit)")
            data= (input(">"))