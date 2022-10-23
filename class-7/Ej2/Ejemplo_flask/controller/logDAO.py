from asyncio import exceptions
import json
import sqlite3
from model.log import Log

class LogDao:
    def __init__(self,db):
        self.db=db

    def get_all(self,numPage,sizePage):
        """ this functions returns all logs stored in db
        """        
        print("numPage:"+str(numPage))
        print("sizePage:"+str(sizePage))
        offset=int(numPage)*int(sizePage)
        c = self.db.cursor()
        c.execute("SELECT * FROM Log limit ? offset ? ;",(sizePage,offset))
        d = c.fetchall()			
        c.close()
        return json.dumps(d)    

    def add_log(self,newLog):
        """ this functions add a new log to the db(the log is passed as a parameter)
        """        
        print(newLog)
        try:
            c = self.db.cursor()     
            c.execute("INSERT INTO  Log (id_device,state,timestam) VALUES (?, ?,?)",(newLog.getIdDevice(),newLog.getState(),newLog.getTimeStamp()))
            self.db.commit()
            print("records:",c.rowcount)
        except sqlite3.Error as error:
            print("\"state\":\"ERROR\"")
            
        finally:    
            c.close()                
            return "ok"

          