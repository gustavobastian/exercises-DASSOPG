#! /usr/bin/python3

import myconfig

#dictionary where are stored the parameters
parameters={}
#file
filenameLocal="./config.txt"

response= 1

myconfig.read_config(filenameLocal , parameters)


while(response>0):
    print(parameters)
    response= int(input("Desea modificar algo? (1-Si ,0-No) :"))
    if(response==1):
        response2= int(input("Que Desea modificar?  1,2 o 3 :"))
        modification= input("Ingrese nuevo valor: ")
        if(response2==1):
            parameters.update({'Name': modification})
        elif(response2==2):
            parameters.update({'Lastname': modification})    
        elif(response2==3):
            parameters.update({'Information': modification})        
        else: 
            print("Error")    
            response=0
        myconfig.save_config(filenameLocal, parameters)
    else: 
         print("Adios")    
         exit()
