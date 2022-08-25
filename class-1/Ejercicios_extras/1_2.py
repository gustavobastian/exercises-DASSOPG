#! /usr/bin/python3

from math import pi,sqrt
import os 

os.system('clear')
nombre = input("Ingrese su Nombre: ")
os.system('clear')
print("Bienvenido "+nombre)
input("PRESIONA CUALQUIER COSA PARA CONTINUAR")
response = 1

def perim_area_rectangle(width, height):
        print("Perim="+str(2*width+2*height))
        print("Area="+str(width*height))

def perim_area_circle(radius):
    print("Perim="+str(2*pi*radius))
    print("Area="+str(pi*radius*radius))

def volume_esphere(radius):
    print("Volume="+str(radius*radius*radius*pi*4/3))

def area_rectangle(x1,x2,y1,y2):
    width_local=abs(x2-x1)
    height_local=abs(y2-y1)
    perim_area_rectangle(width_local,height_local)

def hipotenuse(cat1,cat2):
    hipo=sqrt(cat1*cat1+cat2*cat2)
    print("hipotenuse:"+str(sqrt))

while response != 0 :
    os.system('clear')
    print("*************************************************")
    print("*Que desea hacer:                               *")
    print("*0: Salir                                       *")
    print("*1: calcular area y perimetro de rectangulo     *")
    print("*2: calcular area y perimetro de circulo        *")
    print("*3: calcular volumen de esfera                  *")
    print("*4: calcular area de rectangulo con coordenadas *")
    print("*5: calcular hipotenusa                         *")
    print("*************************************************")
    response=int(input(">"))

    if(response>6): input("Error : PRESIONA CUALQUIER COSA PARA CONTINUAR")
    elif response==1:
        os.system('clear')
        print("calculando area de rectangulo")
        numero1=int(input("Ingresa base: "))
        numero2=int(input("Ingresa altura: "))
        perim_area_rectangle(numero1,numero2)
        input("PRESIONA CUALQUIER COSA PARA CONTINUAR")
    elif response==2:
        os.system('clear')
        print("calculando area de circulo")
        numero1=int(input("Ingresa radio: "))        
        perim_area_circle(numero1)
        input("PRESIONA CUALQUIER COSA PARA CONTINUAR")    
    elif response==3:
        os.system('clear')
        print("calculando volumen de esfera")
        numero1=int(input("Ingresa radio: "))        
        volume_esphere(numero1)
        input("PRESIONA CUALQUIER COSA PARA CONTINUAR")        
    elif response==4:
        os.system('clear')
        print("calculando area de rectangulo por coordenadas")
        numero1=int(input("Ingresa x1: "))
        numero2=int(input("Ingresa x2: "))
        numero3=int(input("Ingresa y1: "))
        numero4=int(input("Ingresa y2: "))
        area_rectangle(numero1,numero2,numero3,numero4)
        input("PRESIONA CUALQUIER COSA PARA CONTINUAR")    
    elif response==5:
        os.system('clear')
        print("calculando hipotenusa")
        numero1=int(input("Ingresa Cateto1: "))
        numero2=int(input("Ingresa Cateto2: "))        
        hipotenuse(numero1,numero2)
        input("PRESIONA CUALQUIER COSA PARA CONTINUAR")        
    else : input("PRESIONA CUALQUIER COSA PARA CONTINUAR")   




    
