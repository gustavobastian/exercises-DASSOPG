
from flask import Flask
import sqlite3
import json
from controller.deviceDAO import DeviceDao
from flask import g
#************** Manejo de DB ****************************



class ControllerDevices:
    def __init__(self,app,request,db):
        self.app=app
        self.request=request
        self.db=db
   

    def get_all(self):        
        c = DeviceDao(self.db)        
        return c.get_all()