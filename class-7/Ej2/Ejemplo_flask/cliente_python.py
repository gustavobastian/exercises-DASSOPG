import requests
import json

BASE_URL = "http://localhost:5000"

print("Cliente HTTP para pruebas")

ERROR_L = "error code:"

while True:
    print("\n1) GET a /devices")
    print("2) PUT a /device")
    print("3) GET a /log")
    print("4) POST a /device")
    print("5) Salir")

    op = int(input("Ingrese una opcion:"))

    if op==1:
        r = requests.get(url = BASE_URL+"/devices") 
        if r.status_code==200:
            print(r.text)
        else:
            print(ERROR_L+str(r.status_code))

    elif op==2:
        id_lamp = input("Ingrese ID de lampara:")
        state_lamp = input("Ingrese estado de lampara [0,1]:")
        data = {"state":state_lamp}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.put(url = BASE_URL+"/devices/"+id_lamp,  data=json.dumps(data),headers=headers ) 
        if r.status_code==200:
            print(r.text)
        else:
            print(ERROR_L+str(r.status_code))

    elif op==3:
        page = input("Ingrese numero de pagina:")
        size = input("Ingrese size de pagina:")
        data = {"page":page,"size":size}
        r = requests.get(url = BASE_URL+"/log",params=data) 
        if r.status_code==200:
            print(r.text)
        else:
            print(ERROR_L+str(r.status_code))
    
    elif op==4:
        
        ip_lamp = input("Ingrese IP de lampara:")
        name_lamp = input("Ingrese Nombre de lampara:")
        state_lamp = input("Ingrese estado de lampara [0,1]:")
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {'id_lamp':0,'name':str(name_lamp),'state':int(state_lamp),'ip_lamp':int(ip_lamp)}
        print(json.dumps(data))
        r = requests.post(url = BASE_URL+"/devices", data=json.dumps(data),headers=headers )
        if r.status_code==200:
            print(r.text)
        else:
            print(ERROR_L+str(r.status_code))


    elif op==5:
        break
