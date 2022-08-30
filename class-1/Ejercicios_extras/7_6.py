#! /usr/bin/python3
# some list

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
import time
import os

list=[1,2,3,4,5,4,7]
#list=[1,1,1,1,1,1,1]


def fun1(x,k):
    if ((str(x).isdigit())== True):
        if(x==k):
            return 0,x,0
        elif(x<k):
            return x,0,0
        elif(x>k):
            return 0,0,x
    list1=[]
    list2=[]
    list3=[]
    for i in range(0,len(x)):
        if(x[i]==k): list2.append(x[i])
        elif(x[i]<k): list1.append(x[i])
        else: list3.append(x[i])
    return list1,list2,list3

def fun2(x,k): 
    if ((str(x).isdigit())== True):
        if(x%k==0):
            return x
        else : return 0
    list=[]    
    for i in range(0,len(x)):
        if(x[i]%k==0): list.append(x[i])
    
    return list

data=1
while data != "q":
    os.system('clear')      
    print((list))
    k=4
    c=2
    var=fun1(list,k)
    print("menores que "+str(k))
    print(var[0])
    print("iguales que "+str(k))
    print(var[1])
    print("mayores que "+str(k))
    print(var[2])

    print("multiplos de "+str(c))
    print(fun2(list,c))

    print("want to repeat?(enter q to exit)")
    data= (input(">"))