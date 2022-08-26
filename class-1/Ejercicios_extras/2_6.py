#! /usr/bin/python3
#using dinamic programming for storing the results
from math import pi,sqrt,pow
import os 

os.system('clear')
print("Bienvenido")

tableFactorial = [1,1]

def factorial(x):
    if x<0: return print("error debe ser >0")
    elif x<len(tableFactorial) : return tableFactorial[x]    
    elif x==(len(tableFactorial)) : 
        tableFactorial.append(x*tableFactorial[x-1])
        print(tableFactorial)
        return tableFactorial[x]
    else :
        for i in range (2,x+1):
            tableFactorial.append(i*tableFactorial[i-1])
        return tableFactorial[x]    
    

#array for saving inputs
number=[]
#variable for storing the inputs
localnumber = 1

while localnumber != 0 :
    localnumber = int(input("Ingrese numbero(0 para calcular):"))
    if(localnumber!=0): number.append(localnumber)

for i in range (0, len(number)):
    print("Orden "+str(i)+" Factorial:"+str(factorial(number[i])))    

exit(0)    