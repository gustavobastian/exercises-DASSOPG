#! /usr/bin/python3

from math import pi,sqrt,pow
import os 

os.system('clear')
print("Bienvenido")
number1= int(input("Ingrese Numero1: "))
number2= int(input("Ingrese Numero2: "))

if(number1==number2): 
    print("son nros iguales")
    exit(0)
elif (number1>number2):
    if(number2%2!=0): 
        number2=number2+1
        print(number2)
    while (number1>number2):    
        number2+=2
        if(number1>number2): print(number2)
        
elif (number1<number2):
    if(number1%2!=0): 
        number1=number1+1
        print(number1)
    while (number2>number1):    
        number1+=2
        if(number2>number1): print(number1)
        
exit(0)        