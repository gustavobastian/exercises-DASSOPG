#! /usr/bin/python3
# simple function that writes to a file the contents of a list of tuples

from operator import truediv


lista= [('George', '4312 Abbey Road',22), ('John','54 Love Ave', 21)]


def myfun(x):
    res1 =type(x) is list
    if(res1== True): 
        res2 = type(x[0]) is tuple
        if(res2== True): 
            print ("Correcto")
            ## here we work on the file
            file_object = open("./myFile.csv","w+")
            file_object.write("name,address,age \n")
            for item in x:
                    for i in item:
                        file_object.write(str(i))
                        file_object.write(',')

                    file_object.write("\n")
            file_object.close()

        else : return print("La lista no contiene tuplas")          

    else : return print("No es una lista")    

myfun(lista)    