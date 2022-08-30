#! /usr/bin/python3
# Passwords
from math import pi,sqrt,pow
from operator import truediv
import time
import os

def comparePass(password,localpass):
        if password==localpass:
            return True
        else:
            return False    


def askPass():
    password= "hola mundo"
    passwordCorrect= False
    tried=0
    while passwordCorrect==False:
        os.system('clear')
        tried+=1
        print("Insert Password:")
        passwordInserted=input(">")
        if(comparePass(passwordInserted, password)):
            print("you gain access")
            passwordCorrect=True
        else: 
            os.system('clear')
            print("error")
            time.sleep(tried)
            if(tried>2):
                print("Too many attempts")
                exit(0)


askPass()

