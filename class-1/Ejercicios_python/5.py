#! /usr/bin/python3

def myfun(strP,x):
   # print("value to insert:" +str( x))
    strout=strP.replace(' ',x )
    return strout


myString= "Esto es una prueba para la funcion"
print("resultado:")
print(str(myfun(myString,"|")))