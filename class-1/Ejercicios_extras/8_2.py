#! /usr/bin/python3
# functions in functions

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os

# response to c, if the elements of the list are characters, considering a literal caracter, the uppercase representation
#  will be take as lower value than the lowercase representation... so always showed the lowercase as maximum value


d=[1,2,4,7,5,26,3,4,3,10,11]
dd=["aba","ber","casa","ala","zumatra","tevez","Liba"]


def findMax(x):
    max=x[0]
    for i in range(1, len(x)-1):
        if(x[i]>max): 
            max=x[i]
        else: continue
    return max

def findMax2(x):    
    max=x[0]
    pos=0
    for i in range(1,len(x)-1):
        if((x[i])>max): 
            max=x[i]
            pos=i
        else: continue
    return max,i



##testing



if __name__ == "__main__":
    data=1

    while data != "q":
        x=0
        os.system('clear')      
        print("original:"+str(d))
        print("looking for Max:"+str(findMax(d)))
        print("looking for Max(value,position):"+str(findMax2(d)))
        print("looking for Max(value,position):"+str(findMax2(dd)))
        
        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))  