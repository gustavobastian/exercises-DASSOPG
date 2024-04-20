from asyncio import exceptions
import json
import sqlite3
from model.log import Log

class LogDao:
    def __init__(self,db):
        self.db=db

    def get_all(self,num_page,size_page):
        """ this functions returns all logs stored in db
        """        
        print("numPage:"+str(num_page))
        print("sizePage:"+str(size_page))
        offset=int(num_page)*int(size_page)
        c = self.db.cursor()
        c.execute("SELECT * FROM Log limit ? offset ? ;",(size_page,offset))
        d = c.fetchall()			
        c.close()
        return json.dumps(d)    

    def add_log(self,new_log):
        """ this functions add a new log to the db(the log is passed as a parameter)
        """        
        print(new_log)
        try:
            c = self.db.cursor()     
            c.execute("INSERT INTO  Log (id_device,state,timestam) VALUES (?, ?,?)",(new_log.getIdDevice(),new_log.getState(),new_log.getTimeStamp()))
            self.db.commit()
            print("records:",c.rowcount)
        except sqlite3.Error :#as error:
            print("\"state\":\"ERROR\"")
            
        finally:    
            c.close()                
            

          