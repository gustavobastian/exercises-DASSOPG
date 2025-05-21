#! /usr/bin/python3
import socket
import json
import os
import sys

class Main:

    #this class is the main class and the constructor just create the instance            
    def __init__(self):
        pass

    def main(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("localhost", 4096))
        print("Escuchando puerto "+str(4096)+"...")
        while True:
            (data, addr) = s.recvfrom(128*1024)
            print(data)
            
            

m = Main()
m.main()
