#! /usr/bin/python3
# Printing domino 
from math import pi,sqrt,pow
import os 

os.system('clear')
print("Bienvenido, imprimiendo fichas de domino")

for i in range(0,7):
    for j in range(i,7):
        print ("ficha "+str(i)+":"+str(j))

exit(0)        
