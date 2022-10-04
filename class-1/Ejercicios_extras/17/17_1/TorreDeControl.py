#! /usr/bin/python3
import random
from time import sleep




class avion:
    def __init__(self) :
       self.number=0
    
    def get_number(self):
        return self.number
    
    def set_number(self, number1):
        self.number=number1

    def __str__(self):
        return str("avion:"+str(self.number))    

class torreDeControl:    
    n=0
    def __init__(self):
     self.aterrizar = []
     self.despegar = []
    
    def reconocimiento(self):
        self.n=self.n+1
        avionLocal = avion()
        avionLocal.set_number(self.n)
        x=random.randrange(2)        
        if (x==0): self.despegar.append(avionLocal)
        if (x==1): self.aterrizar.append(avionLocal) 

    
    def acción(self):
        
        
        if((self.despegar)): 
            y=self.despegar.pop(0)
            print("despegó:"+str(y))    
        else:
             if(self.aterrizar):
                print("aterrizó:"+self.aterrizar.pop(0))
            
        return
        
    def __str__(self):
        print("Aviones por aterrizar:")
        print(*self.aterrizar,sep=', ')
        print("Aviones por despegar:")
        print(*self.despegar,sep=', ')
        return " "
    
if __name__ == "__main__":
    torreDeControl = torreDeControl()
    d=0
    while 1:
        d=d+1
        torreDeControl.reconocimiento()
        print(torreDeControl)
        if(d%3==0): torreDeControl.acción()
        sleep(1)
