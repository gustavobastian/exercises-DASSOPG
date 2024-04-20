#! /usr/bin/python3

from math import pi,sqrt
import os 

CONTINUAR= "presiona tecla para continuar"

def algo1(x1,x2):    
    print("1:"+str(x1)+"+"+str(x2)+"="+ str(x1 + x2))
    print("2:"+str(x1)+"x"+str(x2)+"="+ str(x1 * x2))
    print("3:"+str(x1)+"-"+str(x2)+"="+ str(x1 - x2))
    print("4:"+str(x1)+"/"+str(x2)+"="+ str(x1 / x2))


def algo2(x1):    
    for i in range(0,10):
        print( str (x1)+" x "+str(i)+" = "+str(x1*i))


def algo3(x2):    
    if(x2==0): return 1
    elif(x2==1): return 1
    else : return x2*algo3(x2-1)

##testing

if __name__ == "__main__":
        os.system('clear')

        response=1
        while(response>0):
            os.system('clear')
            print("Que desea hacer(si presionas otra tecla, el sistema sale):")
            print("1: operaciones entre 2 nros")
            print("2: tabla de multiplicar de 1 nro")
            print("3: Factorial de 1 nro")
            response=int(input(">"))
            if(response>3): 
                print("saliendo")
                response=0
            elif(response==1):
                os.system('clear')
                print("operaciones entre 2 nros")
                num1=int(input("numero1: "))    
                num2=int(input("numero2: "))    
                algo1(num1,num2)
                input(CONTINUAR)
            elif(response==2):
                os.system('clear')
                print("Tablas de multiplicacion")
                num1=int(input("número: "))              
                algo2(num1)
                input(CONTINUAR)    
            elif(response==3):
                os.system('clear')
                print("Factorial")
                num1=int(input("número: "))              
                print(str(num1)+"! = "+ str(algo3(num1)))
                input(CONTINUAR)        
            else: continue    