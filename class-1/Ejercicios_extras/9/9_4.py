#! /usr/bin/python3
# counting dictionaries

from cmath import atan
from math import atan2, pi,sqrt,pow,cos
from operator import truediv
import random
from syslog import LOG_UPTO
import time
import os

def countingCharWord(word):
    charW={}
    for i in range(0,len(word)):  
        if(charW.get(word[i])==None):             
                charW.update({str(word[i]):1})
        else:             
            aux=charW.get(str(word[i]))
            aux+=1                        
            charW.update({str(word[i]):aux})
    return charW

def countingCharPhrase(text):
    textChar={}
    for i in range(0,len(text)):  
        if(textChar.get(text[i])==None):             
                textChar.update({str(text[i]):1})
        else:             
            aux=textChar.get(str(text[i]))
            aux+=1                        
            textChar.update({str(text[i]):aux})
    return textChar



def countingChar(text):
    textS= text.split(" ")
    alldic=countingCharPhrase(text)
    mydicW={}
    mydicW2={}      
    for i in range(0,len(textS)):  
        if(mydicW.get(textS[i])==None):       
                val=  countingCharWord(textS[i])    
                mydicW.update({str(textS[i]):val})
                mydicW2.update({str(textS[i]):len(textS[i])})
                
        else:             
            continue
    return mydicW,mydicW2,alldic
##testing

if __name__ == "__main__":
    text= "este es un texto que posee muchas palabras extraordinariamente largas , y es bonito"
    data=1
    lista={}
    while data != "q":
        x=0
        os.system('clear')      
        
        
        val=  countingChar(text)      
        print(val[0])
        print("******************")
        print(val[1])
        print("******************")
        print(val[2])
        
    
        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))