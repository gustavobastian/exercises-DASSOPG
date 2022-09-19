from http import server


class Posicion:    
    def __init__(self,xP,yP):
        """
        constructor:
        @params: 
        xP, number 
        yP, number
        """

        self.x = xP
        self.y = yP

    def setX(self,xP):         
        self.x = xP

    def setY(self,yP):
        self.y = yP

    def getX(self):
        return(self.x)

    def getY(self):
        return self.y 



class Personaje:
    vida= 0
    velocidad=0    
    foot=0
    def __init__(self,vidaP,velocidadP,posicionP) :
        self.posicion=Posicion(posicionP.getX(),posicionP.getY())
        self.velocidad=int(velocidadP)
        self.vida=int(vidaP)
        self.moviendo= False

    def recibirAtaque(self,valor):
        """
        @params value: number with indication of how many life is losing 
        """
        if(self.vida<int(valor)): 
            self.vida=0
            raise Exception("dead")
        else:
            self.vida=self.vida-int(valor)    

    def mover(self,position):
        """
        @params position: destiny position
        """        
        self.posicionFinal= Posicion(position.getX(),position.getY())
        self.moviendo= True

    def moviendose(self):
        """functions that is called every 0,5 seconds in order to move the person        
        """
        "natural pass: 0,5 * velocity"            
        if(self.foot==0):
                if(abs((self.posicionFinal.getX()-self.posicion.getX()))<1*(self.velocidad)):   
                    self.posicion.setX(self.posicionFinal.getX())
                    self.foot=1                    
                    return
                elif ((self.posicionFinal.getX()-self.posicion.getX())<0):
                    #print(str(self.posicion.getX()))            
                    self.posicion.setX(((self.posicion.getX())-self.velocidad))
                    self.foot=1
                    return
                elif ((self.posicionFinal.getX()-self.posicion.getX())>0):
                    #print(str(self.posicion.getX()))
                    self.posicion.setX((self.posicion.getX()+self.velocidad))
                    self.foot=1
                    return
        if(self.foot==1):
                if(abs((self.posicionFinal.getY()-self.posicion.getY()))<1*(self.velocidad)):   
                    self.posicion.setY(self.posicionFinal.getY())     
                    self.foot=0
                    return                    
                elif ((self.posicionFinal.getY()-self.posicion.getY())<0):
                    #print(str(self.posicion.getY()))            
                    self.posicion.setY(((self.posicion.getY())-self.velocidad))
                    self.foot=0
                    return
                elif ((self.posicionFinal.getY()-self.posicion.getY())>0):
                    #print(str(self.posicion.getY()))
                    self.posicion.setY((self.posicion.getY()+self.velocidad))
                    self.foot=0
                    return        

            
    def getPosition(self):
        return str(self.posicion.getX())+":"+str(self.posicion.getY())

class Soldado(Personaje):
    ataqueV=0
    def __init__(self,posicion,velocidad,vida,ataque):
         super().__init__(posicion,velocidad,vida)         
         self.ataqueV=ataque

    def ataque(self,oponente):
        oponente.recibirAtaque(self.ataqueV)

    def get_soldado(self):
        print("soldado:")
        print("vida:"+str(self.vida))   
        print("posicion:("+self.getPosition()+")")       
        
        
class Campesino(Personaje):
    def __init__(self,posicion,velocidad,vida,cosecha):
        super().__init__(posicion,velocidad,vida)
        def __init__(self,cosecha):
            self.cosecha=cosecha

    def cosechar(self):
        return self.cosecha
                

    def get_campesino(self):
        print("campesino:")
        print("vida:"+str(self.vida))   
        print("posicion:("+self.getPosition()+")")   