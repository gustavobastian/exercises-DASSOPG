#! /usr/bin/python3

from math import pi,sqrt,pow
import os 

def calc(c):
    value= c*9/5+32
    return value

response=1

while response != "q":
    os.system('clear')
    print("calculador de temp farenheit: ")
    temp=float(input("temperatura en ºC: ")) 

    print("temperatura en F: "+str(calc(temp)))
    print("presione enter para seguir(con 'q' se sale del programa ):")
    response=input(">")