#! /usr/bin/python3
from Mates import Mates
import os

m= Mates(3)

if __name__ == "__main__":
    data=0    
    while data != "0":
        
        os.system('clear')      
        print("\n What do you want to do:")
        print("\n 1:beber mate")
        print("\n 2:cebar mate")
        print("\n 3: salir mate")
        d=int(input(">"))
        if(d==1):
            try:
                m.beber()
            except Exception as e: 
                print(e )
        if(d==2):
            try:
                m.cebar()
            except Exception as e: 
                print(e)
        if(d==3):
            exit(0)

        if(d<1 or d>3):
            print("opcion incorrecta")                    


        
        print("\n want to repeat?(enter q to exit)")
        data= (input(">"))
        if(data=='q'):exit(0)