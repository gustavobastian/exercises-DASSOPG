#! /usr/bin/python3

import requests
import json
import time
import signal
import socket

BASE_URL = "http://localhost:5000"
"""handler for clean quit
"""
def handler(sig, frame):
    #print(sig)
    print("saliendo en forma ordenada")
    exit(0)

ERROR_L="error code:"

signal.signal(signal.SIGINT, handler)

if __name__ == '__main__':
	print("Cliente HTTP para accionar lamparas")

	r = requests.get(url = BASE_URL+"/devices")
	if r.status_code!=200:
		print(ERROR_L+str(r.status_code))
		exit(0)
	localtable=json.loads(r.text)

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	
	while True:
		time.sleep(5)
		data=[]
		r = requests.get(url = BASE_URL+"/devices")
		if r.status_code!=200:			
			print(ERROR_L+str(r.status_code))
			exit(0)			
		data=json.loads(r.text)
		
					
		for i in range(0,len(localtable)):
			
			if(localtable[i][3]!=data[i][3]):
				
				s.connect((data[i][2], 4096))
				if(data[i][3]==1):
					value=">ST:ON\n"
				else:
					value=">ST:OFF\n"	
				s.send(bytearray(value.encode("UTF-8")))
				
			#guardo la última tabla
			localtable=[]
			localtable=data
			
	s.close()	
