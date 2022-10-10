from asyncio import exceptions
import json
import sqlite3
from model.device import Device

class DeviceDao:
    def __init__(self,db):
        self.db=db

    def get_all(self):
        """This return a list of all the devices in the database
        """        
        c = self.db.cursor()
        c.execute("SELECT * FROM Devices")
        d = c.fetchall()			
        c.close()
        return json.dumps(d)    

    def add(self,newDevice):
        """This function adds a new device to the database
        """
        try:
            c = self.db.cursor()     
            c.execute("INSERT INTO  Devices (name,ip,status) VALUES (?, ?,?)",[newDevice.getName(),newDevice.getIp(),newDevice.getState()])
            self.db.commit()
            print("records:",c.rowcount)

        except sqlite3.Error as error:
            print("error:",error)
            
        finally:    
            c.close()        
            return "ok"

    def set_state(self,id,state):
        """This function modify the state of the device
        """
        print(len(state))
        if ((len(state) ==1)) :
            try:
                c = self.db.cursor()     
                c.execute("UPDATE Devices SET status=? Where id=?",[state,id])
                self.db.commit()
                print("records:",c.rowcount)

            except sqlite3.Error as error:
                print("error:",error)
                
            finally:    
                c.close()        
                return "ok"        
        else:
               return "return  invalid new state"        