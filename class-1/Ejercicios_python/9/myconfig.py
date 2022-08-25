
"""
this function reads the configuration files and update the dictionary called parameters
"""
def read_config(filename, parameters):
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
            
            parameters.update([x])          
        
      #  print("Diccionario generado:")
      #  print(parameters)

        file_object.close()
        return 
    except (IOError, OSError) as e: print("Error archivo no encontrado o permisos equivocados")
    
"""
This function is saves the configuration parameters passed in the dicP dictionary in the file 
pointed by filename variable
"""
def save_config(filename,dictP):
    print(filename)
    print(dictP)

    try:
        file_object = open(filename,"w+")

        for item in dictP:                    
                        file_object.write(str(item))
                        file_object.write('=')
                        file_object.write(dictP.get(item))
                        file_object.write("\n")

        file_object.close()
    except (IOError, OSError) as e: print("Error archivo no encontrado o permisos equivocados")


    return print("ok")

