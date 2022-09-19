#! /usr/bin/python3
import os
import signal
import time
from LinkedList import LinkedList,Node

class LinkedOrderedList(LinkedList):
    def __init__(self):
      super().__init__()

      # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        
        if(self.head ):            
            current = self.head            
            if(newNode.data<current.data):
                newNode.next = current
                self.head=newNode
                return
            while(current.next!=None):                   
                if(current.next.data>newNode.data): break
                current = current.next         

            newNode.next = current.next     
            current.next = newNode
            return
        else:
            self.head = newNode

# insertion method for the linked list
    def append(self, data):
        newNode = Node(data)
        
        if(self.head ):            
            current = self.head            
            if(newNode.data<current.data):
                newNode.next = current
                self.head=newNode
                return
            while(current.next!=None):                   
                if(current.next.data>newNode.data): break
                current = current.next         

            newNode.next = current.next     
            current.next = newNode
            return
        else:
            self.head = newNode


"""handler for clean quit
"""
def handler(sig, frame):
    #print(sig)
    print("saliendo en forma ordenada")
    exit(0)

if __name__ == "__main__":
    i=0
    j=10
    LL = LinkedOrderedList()
    LL2 = LinkedOrderedList()
   
    while i<10:
        i=i+1               
        LL.insert(i)
        LL2.insert(j)
        j=j-1 
    
    print(LL)
    print(LL2)
    print("extend")
    LL.append(24)
    
    print(LL)            