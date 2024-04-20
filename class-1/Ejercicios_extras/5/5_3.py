#! /usr/bin/python3
# Passwords
from math import pi,sqrt,pow
from operator import truediv
import time
import os

def compare_pass(password,localpass):
        if password==localpass:
            return True
        else:
            return False    


def ask_pass():
    password= "hola mundo"
    password_correct= False
    tried=0
    while password_correct==False:
        os.system('clear')
        tried+=1
        print("Insert Password:")
        password_inserted=input(">")
        if(compare_pass(password_inserted, password)):
            print("you gain access")
            password_correct=True
        else: 
            os.system('clear')
            print("error")
            time.sleep(tried)
            if(tried>2):
                print("Too many attempts")
                exit(0)


ask_pass()

