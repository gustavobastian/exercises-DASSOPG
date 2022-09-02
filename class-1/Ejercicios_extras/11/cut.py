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

def cut(filename):
    file_obj=open(filename,"r")
    lines=file_obj.readlines()
    linesS=[]
    for i in range(0, len(lines)):
        linesS.append(lines[i].split(","))
    return linesS

def printCampos(filelista,listaCampos2,lim):    
    ll=len(listaCampos2)-1
    listaCampos=(listaCampos2[1:ll]).split(",")
    #print(str(listaCampos))
    output=""
    var=""
    for i in range(0, len(filelista)):
        var=""
        for j in range(0, len(listaCampos)):               
            var+=(f"{lim}{filelista[i][(int(listaCampos[j]))]}")
        var+="\n"    
        output+=var    
    print(output)


##testing

if __name__ == "__main__":
    
        x=0
        os.system('clear')      
        a = (sys.argv[1])
        b = (sys.argv[2])                
        c = (sys.argv[3])                
       # print(f"{a}")
       # print(f"{b}")
        lista = cut(a)   
        printCampos(lista,c,b)   


        
        
        