#! /usr/bin/python3

from math import pi,sqrt,pow
import os 

def calculo(c,x,n):
    value= c*pow((1+(x/100)),n)
    return value


os.system('clear')
print("Bienvenido al calculador de ganancias")
monto_inicial=float(input("Ingrese cantidad de USD: "))
tasa=float(input("Ingrese tasa de interes: "))
nro_años=int(input("Numero de años: "))
print("Resultado: ")
print("Su capital final es: "+str(calculo(monto_inicial,tasa,nro_años)))