class Log:    
    
    def __init__(self, id=0, id_device=0,state=False,timestamp=None):
        self.id=id
        self.id_device=id
        self.state=state
        self.timeStamp=timestamp

    def getId(self):
        return self.id    

    def getIdDevice(self):
        return self.id_device

    def getState(self):
        return self.state
    
    def getTimeStamp(self):
        return self.timeStamp
    

    def setId(self,number):
        self.id=number    

    def setIdDevice(self,number):
        self.id_device=number

    def setState(self,state):
        self.state=state
    
    def setTimeStamp(self,timestamp):
        self.timeStamp=timestamp

    def __str__(self):
        return "log=>id:"+str(self.id)+"|device_id:"+str(self.id_device)+"|time_stamp:"+str(self.timeStamp)+"|:state "+str(self.state)

    