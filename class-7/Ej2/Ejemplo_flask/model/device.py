from os import stat


class Device:   
    
    def __init__(self,idP=0,ipP=0,nameP=None,stateP=False):
        self.id=idP
        self.ip=ipP
        self.name=nameP
        if(stateP==0 or stateP==1):
            self.state=stateP
        else:self.state=0    

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getIp(self):
        return self.ip

    def getState(self):
        return self.state

    
    def setName(self,name):
        self.name=name

    def setIp(self,ipp):
        self.ip=ipp
    
    def setId(self,ipp):
        self.id=ipp

    def setState(self,stateP):
        self.state=stateP    

    def __str__(self):
        return "device=>id:"+str(self.getId())+"|ip:"+str(self.getIp())+"|name:"+str(self.getName())+"|state:"+str(self.getState())

    
