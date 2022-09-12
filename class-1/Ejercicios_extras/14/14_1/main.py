#! /usr/bin/python3
from botella_corcho import Botella,Corcho,Sacacorchos


c1= Corcho("Laudrup")
c2= Corcho("Romario")
c3= Corcho("Messi")

b1= Botella()
b2= Botella()
b3= Botella()

b1.set_corchoLocal(c1)
b2.set_corchoLocal(c2)
b3.set_corchoLocal(c3)

SC=Sacacorchos()

if __name__ == "__main__":
    SC.destapar(b1)
    print(SC.get_corchoName())
    SC.limpiar()    
    SC.destapar(b2)    
    print(SC.get_corchoName())