#! /usr/bin/python3
# some inversion list

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
dd= ('Toto','Arro','A')
list.append(dd)

#uses auxiliar list
def fun(data):
    list=[]
    for i in range(len(data)):        
        list.append(data[-i])        
    return list    

# do not use auxiliar list
def fun2(data):
    pivot=[]
    for i in range(0,int(len(data)/2)):        
        pivot=data[i]
        data[i]=data[int(len(data))-i-1]
        data[int(len(data))-i-1]=pivot
        
    return list        

##testing

if __name__ == "__main__":
    data=1
    while data != "q":
        os.system('clear')      

        print(list)    
        print(fun2(list))
        
        print("want to repeat?(enter q to exit)")
        data= (input(">"))