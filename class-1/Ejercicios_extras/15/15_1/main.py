#! /usr/bin/python3
from papeles import Papel
from birome import Birome
from marcador import Marcador
import os

p=Papel("")
b=Marcador(5)
if __name__ == "__main__":
    data=0    
    while data != "0":
        
        os.system('clear')      
        print("\n What do you want to do:")
        print("\n 1:Agregar palabra")
        print("\n 2:imprimir")
        print("\n 3: recargar")
        print("\n 4: salir papel")
        d=int(input(">"))
        if(d==1):
            try:
                data=(input("Ingresar palabra>"))
                b.escribir(data,p)
            except Exception as e: 
                print(e )
        if(d==2):
            try:
                print(p)
            except Exception as e: 
                print(e)
        if(d==3):
            try:
                value=int(input("Cuanto:"))
                b.recargar(value)
            except Exception as e: 
                print(e)        
        if(d==4):
            exit(0)

        if(d<1 or d>3):
            print("opcion incorrecta")                    


        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))
        if(data=='q'):exit(0)