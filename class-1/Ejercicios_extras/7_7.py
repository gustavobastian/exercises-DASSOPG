#! /usr/bin/python3
# some list

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
import time
import os
##generating list of tuples
list = []
dd= ('Perex','Juan','R')
list.append(dd)
dd= ('Pwex','auan','R')
list.append(dd)
dd= ('Estero','Prio','D')
list.append(dd)
dd= ('Casual','Lamber','A')
list.append(dd)


def fun(data):
    list=[]
    for i in range(len(data)):
        str=data[i][1]+" "+data[i][2]+". "+data[i][0]
        list.append(str)        
    return list    
    

data=1
while data != "q":
    os.system('clear')      

        
    print(fun(list))
    
    print("want to repeat?(enter q to exit)")
    data= (input(">"))