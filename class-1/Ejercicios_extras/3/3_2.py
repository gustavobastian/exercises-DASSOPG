#! /usr/bin/python3
# Playing with time
from math import pi,sqrt,pow
import os
from turtle import st 

os.system('clear')
print("Bienvenido, jugando con fechas")


def time_to_seconds(hour, minute, second):
        return hour*3600 + minute*60 + second

def seconds_to_time(seconds_total):
    hour= int(seconds_total/3600)
    minutes= int((seconds_total%3600)/60)
    seconds= int(((seconds_total%3600)%60)%60)
    print("time:"+str(hour)+":"+str(minutes)+":"+str(seconds))


stringHora1=(input("Ingrese tiempo 1(hh,min,seg):"))
splittedHour1=stringHora1.split(",")
#print(splittedHour1)
if (len(splittedHour1)!=3): 
    print("error en cantidad de parametros")
    exit(0)

stringHora2=(input("Ingrese tiempo 2(hh,min,seg):"))
splittedHour2=stringHora2.split(",")

if len(splittedHour2)!=3: 
    print("error en cantidad de parametros")
    exit(0)



seconds1=time_to_seconds(int(splittedHour1[0]),int(splittedHour1[1]),int(splittedHour1[2]))
seconds2=time_to_seconds(int(splittedHour2[0]),int(splittedHour2[1]),int(splittedHour2[2]))


secondsTotal=seconds1+seconds2

print("Resultado:")
seconds_to_time(secondsTotal)




