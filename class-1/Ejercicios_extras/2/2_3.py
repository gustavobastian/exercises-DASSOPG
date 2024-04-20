#! /usr/bin/python3

from math import pi,sqrt,pow
import os 

table={}
def calcf(c):
    value= c*9/5+32
    return value

def calcc(f):
    value= ((f-32)*5)/9
    return value

def generate_table(table):
    for i in range(0,12):        
        table.update([(i*10,calcc(i*10))])

def print_table(table):
    print("ºC  :    ºF   ")
    for i in range(0,12):
        print(str(i*10) +" :"+ str(table[i*10]))

generate_table(table)
print_table(table)

