from socket import CAN_BCM_TX_ANNOUNCE
from birome import Birome

class Marcador(Birome):
    def __init__(self,cant_tinta):
        super().__init__(cant_tinta)
        self.cantidad_tinta=cant_tinta

    def recargar(self,value):
        self.cantidad_tinta=self.cantidad_tinta+value

    def escribir(self, texto, papel):        
        for i in range(0, len(texto)):
            if(self.cantidad_tinta==0): raise Exception("Sin tinta")
            else:
                papel.escribir(texto[i])
                self.cantidad_tinta-=1
