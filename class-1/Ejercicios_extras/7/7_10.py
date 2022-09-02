#! /usr/bin/python3
# paragraphs

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os

long=20
text= "Pedrito fue a la escuela hasta que empezo a llover mucho y debió encontrar la forma de divertirse"

def order(a,b):
    data=a.split(" ")
    
    output=[]
    outputl=""
    l=0
    for i in range(len(data)):          
        if(l<(b-len(data[i])+1)):
            outputl+=" "+str(data[i])
            l+=len(data[i])
        else:
            output.append(outputl)    
            outputl=data[i]
            l=0
    output.append(outputl)        
    return output

data=1
while data != "q":
    os.system('clear')      
    
    print(order(text,long)    )
    
    print("want to repeat?(enter q to exit)")
    data= (input(">"))