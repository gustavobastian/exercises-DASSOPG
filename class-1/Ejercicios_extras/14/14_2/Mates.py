class Mates:
    cebadas=0
    estado="vacío"
    def __init__(self, n):
        self.MaximasCebadas=n
        self.estado="vacío"
        self.cebadas=n
    
    def cebar(self):
        if(self.estado=="lleno"): raise Exception("Cuidado te quemaste")
        else : self.estado="lleno"

    def beber(self):
        if(self.estado=="vacío"): raise Exception("El mate está vacío")
        else:
            self.estado="vacío"
            if(self.cebadas!=0):
                self.cebadas=self.cebadas-1
            else : 
                self.cebadas=0   
                print("Advertencia el mate está lavado")
