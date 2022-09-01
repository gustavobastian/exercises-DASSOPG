#! /usr/bin/python3
# 2D vectors

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
import time
import os


def cross_product(x,y):    
    magx=mag(x)
    angx=ang(x)*pi/180
    magy=mag(y)
    angy=ang(y)*pi/180

    theta= (angx-angy)

    
    return abs(magx)*abs(magy)*cos(theta)

def mag(x):
    xx=(x[2]-x[0])
    yy=(x[3]-x[1])
    return sqrt(xx*xx+yy*yy)
def ang(x):
    xx=(x[2]-x[0])
    yy=(x[3]-x[1])    
    return (atan2(yy,xx)*180)/pi


def areParallel(x,y):
   if (ang(x)==ang(y)) : return True
   else:
    return False

def areOrthogonal(x,y):
   if (ang(x)-ang(y)%180==0) : return False
   elif (ang(x)-ang(y)%90==0) : return True
   else:
    return False

def strV2tupleV(xx):    
    x=xx.split(',')
    if((len(x)!=4)): 
        print("Error")
        return(0,0)         
    else:
        return int(x[0]),int(x[1]),int(x[2]),int(x[3]) 

if __name__ == "__main__":
        
    data=1
    while data != "q":
        os.system('clear')      
        
        firstV=str(input("First vector (ej x1,y1,x2,y2):"))            
        secondV=str(input("Second vector (ej x1,y1,x2,y2):"))        
        fV=strV2tupleV(firstV)
        sV=strV2tupleV(secondV)
        
        
        print("vector1 magnitude | angle:")
        print(fV)
        print(str(mag(fV))+"|"+str(ang(fV)))
        print("vector2 magnitude | angle:")
        print(sV)
        print(str(mag(sV))+"|"+str(ang(sV)))
        
        
        print("Are parallel?")
        print(areParallel(fV,sV))

        print("Are orthogonal?")
        print(areOrthogonal(fV,sV))
        
        print("V1.V2 (=|V1|*|V2|*cos(angleº))?")
        print(cross_product(fV,sV))
        
        #print(escalar_product(fV,sV))
        

        print("want to repeat?(enter q to exit)")
        data= (input(">"))