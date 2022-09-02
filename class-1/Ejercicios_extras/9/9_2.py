#! /usr/bin/python3
# counting dictionaries

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os
from tkinter import Y

phrase= "este mundo es precioso y es muy feliz con yogurt y helado y mentolina y musica y sin comas y sin parentesis"



def tirar_dados(size,output):
    
    for i in range(size):
        x=random.randint(1,6)
        y=random.randint(1,6)
        sum=x+y
        print(str(i)+":("+str(x)+"-"+str(y)+")")       
        
        if(output.get(str(sum))==None):             
            output.update({str(sum):1})
        else:             
            aux=output.get(str(sum))
            aux+=1                        
            output.update({str(sum):aux})

    return output    


def frase_a_diccionario(x):
    lista= x.split(' ')
    mydic={}    
    for i in range(0,len(lista)):        
        if(mydic.get(lista[i])==None): 
            #print(" not found")
            mydic.update({str(lista[i]):1})
        else:
            #print("found")
            aux=mydic.get(lista[i])
            aux+=1
            mydic.update({str(lista[i]):aux})
         #print(str(x[i][0])+":"+str(x[i][1]))
    return mydic 

def frase_a_diccLetras(x):
    lista= x.split(' ')
    mydic={}    
    for i in range(0,len(lista)):        
        for j in range(0,len(lista[i])):        
            if(mydic.get(lista[i][j])==None): 
                #print(" not found")
                mydic.update({str(lista[i][j]):1})
            else:
                #print("found")
                aux=mydic.get(lista[i][j])
                aux+=1
                mydic.update({str(lista[i][j]):aux})
            #print(str(x[i][0])+":"+str(x[i][1]))
    return mydic     



##testing

if __name__ == "__main__":
    values={}
    data=1
    while data != "q":
        x=0
        os.system('clear')      
        
        print(frase_a_diccionario(phrase))
        print(frase_a_diccLetras(phrase))
        values=tirar_dados(6,values)
        print("values updated:"+str(values))
        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))