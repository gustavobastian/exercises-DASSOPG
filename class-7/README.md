# Flask sqlite3 practice
Simple backend that uses  flask and sqlite3.\
The program cliente_python lets the user add a new device, modify the state(on/off), list devices or print the log of modifications.\
The program luz_service.py simulates a device, that receives instructions by using udp socket on port 4096, and ip 'localhost' and prints the message to console.
The program accionador_lampara.py ask for the list of states to the server every 5 seconds.

How to run the programs :\
``` 
[new terminal]:
cd Ej2/Ejemplo_flask
python3 index.py 
[new terminal]:
cd Ej2/Ejemplo_flask
python3 cliente_python.py
[new terminal]:
cd Ej5
python3 luz_service.py
[new terminal]:
cd Ej4
python3 accionador_lampara.py

```

