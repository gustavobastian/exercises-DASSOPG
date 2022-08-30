#! /usr/bin/python3
# characters

from math import pi,sqrt,pow
from operator import truediv
import random
import time
import os




def inverted(x):
    d=str(x)
    z=len(d)
    i=1
    s=""
    while i < len(d):                        
            s+=d[-i]            
            i+=1
    s+=d[0]                 
    return s   


def onlyconsonants(x):
    output=""
    for i in range (0,len(x)):
        if ( (x[i]!='A') and (x[i]!='a') and (x[i]!='E') and (x[i]!='e') and (x[i]!='I') and (x[i]!='i')  and (x[i]!='O') and (x[i]!='o') and (x[i]!='U') and (x[i]!='u')):
            output+=x[i]    
    return output

def noconsonants(x):
    output=""
    for i in range (0,len(x)):
        if ( (x[i]!='A') and (x[i]!='a') and (x[i]!='E') and (x[i]!='e') and (x[i]!='I') and (x[i]!='i')  and (x[i]!='O') and (x[i]!='o') and (x[i]!='U') and (x[i]!='u')):
            continue
        else:
            output+=x[i]         
    return output    

def repaceConsonant(x):
    output=""
    for i in range (0,len(x)):        
            if(x[i]=='A'):
                output+='E'         
            elif(x[i]=='E'):
                output+='I'             
            elif(x[i]=='I'):
                output+='O'                 
            elif(x[i]=='O'):
                output+='U'    
            elif(x[i]=='U'):
                output+='A'    
            if(x[i]=='a'):
                output+='e'         
            elif(x[i]=='e'):
                output+='i'             
            elif(x[i]=='i'):
                output+='o'                 
            elif(x[i]=='o'):
                output+='u'    
            elif(x[i]=='u'):
                output+='a'   
            else :        
                output+= x[i]   
    return output    

def isPalindrome(x):
    d=inverted(x)
    for i in range(0, len(x)):
        if (x[i]!=d[i]) : return False
        else: continue

    return True    

data=1
while data != "q":
    os.system('clear')      
    
    caractA=(input("character Array:"))            
    
   
    print(onlyconsonants(str(caractA)))
    print(noconsonants(str(caractA)))
    print(repaceConsonant(str(caractA)))
    print(isPalindrome(str(caractA)))
    

    print("want to repeat?(enter q to exit)")
    data= (input(">"))
