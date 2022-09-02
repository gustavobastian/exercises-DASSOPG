#! /usr/bin/python3
# Matrix

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,1,1],[1,1,1],[1,1,1]]
matrix5 = [[1,0,0],[0,1,0],[0,0,1]]

vector = [[1],[1],[1]]

matrix3 = [[1,2,3,1],[4,5,6,1],[7,8,9,1],[1,1,1,1]]
matrix4 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

matrix6 = [[6,-2,2,4],[12,-8,6,10],[3,-13,9,3],[-6,4,1,-18]]



#printing matrix
def pM(x):
    
    for i in range (0, len(x)):
        print(x[i])
    
    return    


def summ(x,y):
    if(len(x)!=len(y)): 
        print("cant sum not similar matrixes")
        return [0]
    elif(len(x[0])!=len(y[0])): 
        print("cant sum not similar matrixes")
        return [0]    
    else:
        mouput=[]
        louput=[]
        for i in range (0, len(x)):
            louput=[]
            for j in range (0, len(x[0])):
                louput.append(x[i][j]+y[i][j])
            mouput.append(louput)    
        return mouput

def productM(xx,yy):

        mouput=[]
        louput=[]

        if(len(xx)!=len(yy[0])): 
            if(len(xx[0])!=len(yy)):
                print("cant perform wrong dimensions")               
                return [0]
            else:     
                x=yy
                y=xx
        else:
            x=xx
            y=yy


        for i in range (0, len(x)):
            louput=[]
            for j in range (0, len(x[0])):
                xx=0
                for d in range (0, len(y[0])):
                    xx+=x[d][j]*y[i][d]
                louput.append(xx)
            mouput.append(louput)                    
        return mouput


def triagSupMatrix(x):    
    
    return x

def liIndep(x):    

    return x


##testing

if __name__ == "__main__":
        data=1
        while data != "q":
            os.system('clear')      
            print("Matrix 1")
            pM(matrix1)    
            print("Matrix 2")
            pM(matrix2)   

            print("Suma:")
            pM(summ(matrix1,matrix2))

            print("Product:")
            pM(productM(matrix1,matrix2))
            print("Product with identity:")
            pM(productM(matrix1,matrix5))
            print("Product with vector:")
            pM(productM(matrix1,vector))
            print("Product with vector:")
            pM(productM(vector,matrix1))

            pM(triagSupMatrix(matrix6))
            
            print("want to repeat?(enter q to exit)")
            data= (input(">"))