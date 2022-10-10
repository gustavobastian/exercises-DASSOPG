from flask import Flask
import sqlite3
import json
from controller.logDAO import LogDao
from model.device import Device
from flask import g

#************** Manejo de DB ****************************



class ControllerLog:
    def __init__(self,app,request,db):
        self.app=app
        self.request=request
        self.db=db
   

    def get(self,numPage,sizePage):        
        
        c = LogDao(self.db)        
        return c.get_all(numPage,sizePage)