#! /usr/bin/python3
# some function that give you the sign
from math import pi,sqrt,pow
import os

tableSign=[
        "Acuario",
        "Piscis", 
        "Aries",
        "Tauro",
        "Geminis",
        "Cancer",
        "Leo",
        "Virgo",
        "Libra",
        "Escorpio",
        "Sagitario",
        "Capricornio",        
    ]

def sign_of(x):    
    data_local=x.split("/")
    data=[int(data_local[1]),int(data_local[0])]
    
    
    if(data[0]==1):
        if(data[1]<21): print( tableSign[11])
        else: print( tableSign[0])
    elif(data[0]==2):
        if(data[1]<20): print(tableSign[0])
        else: print( tableSign[1])    
    elif(data[0]==3):
        if(data[1]<21): print( tableSign[1])
        else: print( tableSign[2]        )
    elif(data[0]==4):
        if(data[1]<22): print( tableSign[2])
        else: print( tableSign[3]            )
    elif(data[0]==5):
        if(data[1]<21): print( tableSign[3])
        else: print(tableSign[4]   )
    elif(data[0]==6):
        if(data[1]<22): print(tableSign[4])
        else: print(tableSign[5])                    
    elif(data[0]==7):
        if(data[1]<24): print( tableSign[5])
        else:print( tableSign[6])                        
    elif(data[0]==8):
        if(data[1]<24): print( tableSign[6])
        else:print( tableSign[7])                            
    elif(data[0]==9):
        if(data[1]<24): print( tableSign[7])
        else:print( tableSign[8])
    elif(data[0]==10):
        if(data[1]<23): print( tableSign[8])
        else:print( tableSign[9])                                    
    elif(data[0]==11):
        if(data[1]<23): print( tableSign[9])
        else:print( tableSign[10])
    elif(data[0]==12):
        if(data[1]<22): print( tableSign[10])
        else: print( tableSign[11])                                            

    

number=1
while number != '0' :
    os.system('clear')
    data=input("Write your birthdate(dd/mm):")
    sign_of(data)
    print("press enter for repeat (0 exits)")
    number=(input(">"))
