#! /usr/bin/python3
# simple function that reads from a file the information and generate a dictionary

def myfun(filename):
    try:
        file_object = open(filename,"r")
        ## reading the file
        lines = file_object.readlines()
        mydic={}

        for item in lines:
            x_initial  = item.split("\n")
            x= x_initial[0].split("=")
            for i in x:                 
                i.strip()            
            
            mydic.update([x])          
        
        print("Diccionario generado:")
        print(mydic)

        file_object.close()
        return 
    except (IOError, OSError) as e: print("Error archivo no encontrado o permisos equivocados")
    

myfun("./config.txt")        