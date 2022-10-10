#! /usr/bin/python3

from crypt import methods
import json
from flask import Flask
import sqlite3
from flask import g
from flask import request
import requests

from controller.controllerDevices import ControllerDevices
from controller.controllerDevice import ControllerDevice
from controller.controllerLog import ControllerLog

app = Flask(__name__)

#************** Manejo de DB ****************************
DATABASE = 'devices.db3'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
#________________________________________________________



@app.route('/devices',methods=['GET', 'POST'])
def devices():
    if request.method == 'GET':    
        """asking for all the devices from the database
        """
        db = get_db()
        controller=ControllerDevices(app,request,db)	
        return controller.get_all()

    elif request.method == 'POST':
        """Adding a new device to the database
        """
        db = get_db()
        controller2=ControllerDevice(app,request,db)	
        controller2.post()
        return 'ok'
    
   
    else: return 'method not supported'

@app.route('/devices/<deviceId>',methods=['PUT','DELETE'])
def set_state_devices(deviceId):
    """altering the state of the device on the table
    """
    if request.method == 'PUT':
        db = get_db()
        data=(request.get_json())
        dataj=json.loads(json.dumps(data))
        newState=dataj['state']        
        controller2=ControllerDevice(app,request,db)	
        controller2.put(deviceId,newState)
        return 'ok'
    elif request.method == 'DELETE':
        """Deleting the device on the table, not implemented yet
        """
        
        print("deleting")
        return 'ok'       
   
    else: return 'method not supported'


@app.route('/log',methods=['GET'])
def log():
    if request.method == 'GET':    
        """asking for all the logs from the database
        """
        #print("here")
        #print(request.args)
        numPage=request.args['page']
        sizePage=request.args['size']
        db = get_db()
        controller=ControllerLog(app,request,db)	
        return controller.get(numPage,sizePage)
    


if __name__ == '__main__':
	app.debug = True
	app.run()
