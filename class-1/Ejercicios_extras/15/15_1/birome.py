from papeles import Papel

class Birome:
    cantidad_tinta=0    
    
    def __init__(self,cantidad):
        self.cantidad_tinta=cantidad
        
    def escribir(self, texto, papel): 
        for i in range(0, len(texto)):
            if(self.cantidad_tinta==0): raise Exception("Sin tinta")
            else:
                papel.escribir(texto[i])
                self.cantidad_tinta-=1

    
