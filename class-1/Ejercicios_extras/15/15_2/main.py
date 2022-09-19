#! /usr/bin/python3
import os
import signal
import time
from GameLib import Posicion,Soldado,Campesino

posicionInicial=Posicion(5,5)
posicionInicial2=Posicion(1,3)
soldado= Soldado(10,2,posicionInicial,11)
posicionFinal=Posicion(-1,15.5)
campesino= Campesino(10,2,posicionInicial2,2)
posicionFinal2=Posicion(10,3)




"""handler for clean quit
"""
def handler(sig, frame):
    #print(sig)
    print("saliendo en forma ordenada")
    exit(0)

if __name__ == "__main__":
    time_local=0
    data=0    
    soldado.mover(posicionFinal)
    campesino.mover(posicionFinal2)
    while data != "0":
        time_local=time_local+1
        os.system('clear')      
        if(time_local==3):
            soldado.ataque(campesino)

        soldado.get_soldado()
        soldado.moviendose()
        campesino.moviendose()
        campesino.get_campesino()
        time.sleep(1)        
        
        
     #   print("\n want to repeat?(enter q to exit)")
     #   data= (input(">"))
     #   if(data=='q'):exit(0)