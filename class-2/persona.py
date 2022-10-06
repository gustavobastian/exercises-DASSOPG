#!  /usr/bin/python3

from numpy import true_divide

class Persona:
    _nombre=""
    _edad=0
    
    def __init__(self,name=None,edad=0):
        """Constructor
        """
        self._nombre=name
        self._edad = edad

    def set_nombre(self,nombre):
        """Function that sets the name of the person
        """
        self._nombre=nombre

    def set_edad(self,edad):
        """Function that sets the age of the person
        """
        self._edad=edad
    
    def get_edad(self):
        """Function that returns the age of the person
        """
        return self._edad

    def get_nombre(self):
        """Function that returns the name of the person
        """
        return self._nombre    

    def print_persona(self):
        """Function that prints the person's data
        """
        print("Nombre: " + str(self._nombre) + "| Edad:"+ str(self._edad))

    def es_mayor_de_edad(self):
        """Function that returns true if the age of the person is >=18
        , in other case returns false
        """
        if(self.get_edad()>=18):
            return True
        else:
            return False

    def es_mayor_que(self, other):
        """Function that returns true if the age of the person is >= of the age
        of the person passed as a parameter, in other case returns false
        """
        if(self.get_edad()>=other.get_edad()):
            return True
        else:
            return False


    @staticmethod
    def get_mayor_que(personA, personB):
        """Function that compares the age of the persons passed as a parameters, and
        returns the one that is older
        """
        if(personA.get_edad()>=personB.get_edad()):
            return personA
        else:
            return personB      

    @staticmethod
    def dump_csv(filename,lista):  
        file_object=open(filename,"w")              
        item="Name,Age\n"
        file_object.write(str(item))
        for i in range (0,len(lista)):
            item=(str(lista[i].get_nombre())+","+str(lista[i].get_edad())+"\n")
            file_object.write(str(item))
        file_object.close()    

    @staticmethod
    def load_csv(filename):  
        lista=[]        
        file_object=open(filename,"r")                      
        d=file_object.readlines()
        file_object.close()
        for i in range (1,len(d)):
            ff=d[i].split("\n")
            f=ff[0].split(",")
            localPersona=Persona(f[0],f[1])
            lista.append(localPersona)
        return lista    
            


if __name__ == "__main__":
    a=Persona("Jorge",32)
    b=Persona("Pedro",45)
    c=Persona("Luisa",22)
    d=Persona("Carlos",72)
    lista=[]
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.append(d)

    Persona.dump_csv("holamundo.csv",lista)
    lista2= Persona.load_csv("holamundo.csv")
    print("imprimiendo lista:")
    for i in range (0,len(lista2)):
        lista2[i].print_persona()

