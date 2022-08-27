#! /usr/bin/python3
# Playing with time
from math import pi,sqrt,pow
import os
from turtle import st 

os.system('clear')
print("Bienvenido, jugando con fechas")


def time_to_seconds(hour, minute, second):
        print("time_to_seconds:"+str( hour*3600 + minute*60 + second))

def seconds_to_time(secondsTotal):
    hour= int(secondsTotal/3600)
    minutes= int((secondsTotal%3600)/60)
    seconds= int(((secondsTotal%3600)%60)%60)
    print("time:"+str(hour)+":"+str(minutes)+":"+str(seconds))


time_to_seconds(2,3,55)    
seconds_to_time(7435)

