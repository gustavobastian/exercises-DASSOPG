VACIO = "vacío"
LLENO = "lleno"
class Mates:
    

    cebadas=0
    estado= VACIO
    def __init__(self, n):
        self.MaximasCebadas=n
        self.estado = VACIO
        self.cebadas=n
    
    def cebar(self):
        if(self.estado== LLENO): raise Exception("Cuidado te quemaste")
        else : self.estado= LLENO

    def beber(self):
        if(self.estado== VACIO): raise Exception("El mate está vacío")
        else:
            self.estado= VACIO
            if(self.cebadas!=0):
                self.cebadas=self.cebadas-1
            else : 
                self.cebadas=0   
                print("Advertencia el mate está lavado")
