#! /usr/bin/python3
# Printing domino 
from math import pi,sqrt,pow
import os 

os.system('clear')
print("Bienvenido, imprimiendo fichas de domino")
numero= int(input("Ingresar el numero maximo que figura en fichas: "))

for i in range(0,numero+1):
    for j in range(i,numero+1):
        print ("ficha "+str(i)+":"+str(j))

exit(0)        
