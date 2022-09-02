#! /usr/bin/python3

from math import pi,sqrt
import os 

os.system('clear')

word= input("Ingrese una palabra que se repetira 1000 veces : ")
wordfill=""
for i in range (0,1000):
    wordfill = wordfill + word + " "

print(wordfill)


