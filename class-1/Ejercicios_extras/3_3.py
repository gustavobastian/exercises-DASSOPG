#! /usr/bin/python3
# 
from math import pi,sqrt,pow
import os
from turtle import st 

os.system('clear')
print("Welcome to calculating triangles areas program")

def norm(x,y):
    return sqrt(x*x + y*y)

def vector_diff(x1,y1,x2,y2):
    return [x1-x2, y1-y2]

def distance(x1,y1,x2,y2):
    vd=vector_diff(x1,y1,x2,y2)
    return norm(vd[0],vd[1])

def normV(x,y):
    xx=x/(norm(x,y))
    yy=y/(norm(x,y))
    return [xx,yy]


def unitary_diff_vector(x1,y1,x2,y2):
    vd=vector_diff(x1,y1,x2,y2)
    output=normV(vd)
    return output    



def proyection(x,y,dx,dy,cx,cy):
    ##first step
    x1=x-cx
    y1=y-cy
    ##second step
    p11=dx*dx
    p12=dx*dy
    p21=p12
    p22=dy*dy
    ##third step
    rx= p11*x + p12*y 
    ry= p21*x + p22*y
    ##fourth step
    return x1+rx, y1+ry


def area(width, height):
    return (width*height)/2

def calculatingArea(x1, y1, x2, y2, x3, y3):
    #Using Herons formula
    #calculating sides
    s1=abs(distance(x1,y1,x2,y2))
  #  print("s1:"+str(s1))
    s2=abs(distance(x2,y2,x3,y3))
   # print("s2:"+str(s2))
    s3=abs(distance(x1,y1,x3,y3))
   # print("s3:"+str(s3))        
    A=((sqrt((s1+s2+s3)*(s2+s3-s1)*(s3+s1-s2)*(s1+s2-s3)))/4)
    return A
"""
vector1= input("Vector 1 coordinates(x|y): ")
vector1_s= vector1.split("|")
vector2= input("Vector 2 coordinates(x|y): ")
vector2_s= vector2.split("|")

vector1_P= [int(vector1_s[0]),int(vector1_s[1])]
vector2_P= [int(vector2_s[0]),int(vector2_s[1])]

vector1_PN=normV(vector1_P[0],vector1_P[1])
vector2_PN=normV(vector2_P[0],vector2_P[1])

output= proyection(vector1_P[0],vector1_P[1] ,vector2_PN[0],vector2_PN[1],0,0)

print("proyection: "+str(output[0])+","+str(output[1]))
"""
answer=calculatingArea(0,0,1,0,1,2)
print("Area:"+str(round(answer,2)))


#print("vector1 norm: ["+str(vector1_PN[0])+","+str(vector1_PN[1])+"]")
#print("vector2 norm: ["+str(vector2_PN[0])+","+str(vector2_PN[1])+"]")
#print(distance(vector1_P[0],vector1_P[1],vector2_P[0],vector2_P[1]))



