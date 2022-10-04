#!/usr/bin/env python3

class Sensores:
	def __init__(self):
		self.temp=19.9
		self.hum=20
	
	def setTemp(self,tempe):
		self.temp=tempe
		
	def setHum(self,hume):
		self.hum=hume
		
	def getTemp(self):
		return self.temp
	
	def getHum(self):
		return self.hum
