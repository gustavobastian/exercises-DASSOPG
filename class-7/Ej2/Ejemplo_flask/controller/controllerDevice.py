from flask import Flask
import sqlite3
import json
from controller.logDAO import LogDao
from controller.deviceDAO import DeviceDao
from model.device import Device
from model.log import Log
import datetime
import time
from flask import g
#************** Manejo de DB ****************************

class ControllerDevice:
    def __init__(self,app,request,db):
        self.app=app
        self.request=request
        self.db=db
   
    def post(self):
        """Add a new the device, the device information comes in the request body
        """
        data=(self.request.get_json())
        dataj=json.loads(json.dumps(data))

        DeviceLocal=Device(dataj['id_lamp'],dataj['ip_lamp'],dataj['name'],dataj['state'])
        c = DeviceDao(self.db)        
        c.add(DeviceLocal)
        
    def put(self,id,state):
        """Modification of the device state
        """        
        newState=state
        c = DeviceDao(self.db)        
        c.set_state(id,newState)

        #generating the new log and adding it to the db
        ts = time.time()
        timestamp=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        newLog=Log(0,id,newState,timestamp)
        d=LogDao(self.db)
        d.add_log(newLog)

        



