#!/usr/bin/env python3

# import urllib library
import signal
from time import sleep
from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "http://localhost:8002/cgi-bin/sensors.py"


"""handler for clean quit
"""
def handler(sig, frame):
    #print(sig)
    print(" \nsaliendo en forma ordenada")
    exit(0)

signal.signal(signal.SIGINT, handler)

  
# store the response of URL
response = urlopen(url)
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
while 1:
    # print the json response
    print(data_json)
    sleep(5)
    response = urlopen(url)
    data_json = json.loads(response.read())
    
