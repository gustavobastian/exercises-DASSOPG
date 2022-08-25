#! /usr/bin/python3

from math import pi,sqrt,pow
import os 

table={}
def calcF(c):
    value= c*9/5+32
    return value

def calcC(f):
    value= ((f-32)*5)/9
    return value

def generateTable(table):
    for i in range(0,12):        
        table.update([(i*10,calcC(i*10))])

def printTable(table):
    print("ºC  :    ºF   ")
    for i in range(0,12):
        print(str(i*10) +" :"+ str(table[i*10]))

generateTable(table)
printTable(table)

