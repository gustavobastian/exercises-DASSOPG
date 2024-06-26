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
        self.data=(request.get_json())
        self.dataj=json.loads(json.dumps(self.data))
        self.newState=self.dataj['state']    
   
    def post(self):
        """Add a new the device, the device information comes in the request body
        """
        data=(self.request.get_json())
        dataj=json.loads(json.dumps(data))

        device_local=Device(dataj['id_lamp'],dataj['ip_lamp'],dataj['name'],dataj['state'])
        c = DeviceDao(self.db)        
        c.add(device_local)
        
    def put(self,id):
        """Modification of the device state
        """                
        c = DeviceDao(self.db)        
        c.set_state(id,self.newState)

        #generating the new log and adding it to the db
        ts = time.time()
        timestamp=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        new_log=Log(0,id,self.newState,timestamp)
        d=LogDao(self.db)
        d.add_log(new_log)

        



