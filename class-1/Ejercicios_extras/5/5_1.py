#! /usr/bin/python3
# some function that give you prom of notes
from math import pi,sqrt,pow
import os




nota=0.0
number=1
prom=0.0
sum=0.0
number_of_notes=0

def calc_prom(number_of_notes,sum):
    prom=sum/number_of_notes
    return prom


while number != '0' :
    os.system('clear')
    note=float(input("Insert new note:"))
    number_of_notes += 1
    sum+=note
    prome=float(calc_prom(number_of_notes,sum))
    print("prom:"+ str(round(prome,2)))
    print("press enter for add other (0 exits)")
    number=(input(">"))
