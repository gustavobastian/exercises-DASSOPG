#! /usr/bin/python3
#summing numbers without using series 
from math import pi,sqrt,pow
import os 

os.system('clear')
print("Bienvenido")

number1= int(input("Ingrese Numero: "))
sum=0

for i in range(1,number1+1):
    sum+=i

print("El resultado es :"+str(sum))
