#!/usr/bin/env python3
from functions import Sensores
s1=Sensores()
s2=str(s1.getTemp())
s3=str(s1.getHum())
#print("Content-Type: text/html\n")
#print("<!doctype html><title>Hello</title><br><h2>"+s2+"</h2><br><h2>"+s3+"</h2>")

print("Content-Type: application/json\n")
print("{\"temp\":"+str(s2)+",\"hum\":\""+str(s3)+"\"}")