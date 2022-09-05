#! /usr/bin/python3
# working with files

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
import sys
from syslog import LOG_UPTO
import time
import os


def cargar_datos(filename):
    if(type(filename)!=str):
        return
    else:
        output={}
        #print(filename)
        f=open(filename,"r")
        lines=f.readlines()
        f.close() 
        for i in range(0,len(lines)):
            linesS=lines[i].split("\n")
            linesSs=linesS[0].split(",")
            output.update({str(linesSs[0]):linesSs[1]})
        return output  

        

def guardar_datos(filename,dic):
        
    if(type(filename)!=str):
        return
    else:
        #print(filename)
        f=open(filename,"w+")
        for i in dic:
            #print(f"{i} : {dic.get(i)}")
            strs=f"{i}, {dic.get(i)}\n"
            f.write(strs)
        f.close()

##testing

if __name__ == "__main__":
        lista={'Name':'gus','pais':'Argentina'}
        os.system('clear')      
        filename="myDic.txt"
        guardar_datos(filename,lista)
        lista2= cargar_datos(filename)
        print(lista2)
       # print(f"{b}")
        
        
        
        
        