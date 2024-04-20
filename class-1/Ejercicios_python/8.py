#! /usr/bin/python3
# simple function that reads from a file the information and generate a dictionary

file="./salida.txt"
mydict= {'Name': 'Gustavo', 'Lastname': 'GustavoLastname', 'Information': 'male'}



def myfun(filename,dict_p):
    print(filename)
    print(dict_p)

    try:
        file_object = open(filename,"w+")

        for item in dict_p:                    
                        file_object.write(str(item))
                        file_object.write('=')
                        file_object.write(dict_p.get(item))
                        file_object.write("\n")

        file_object.close()
    except (IOError, OSError) as e: print("Error archivo no encontrado o permisos equivocados")


    return print("ok")


myfun(file,mydict)