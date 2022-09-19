#! /usr/bin/python3
import os
import signal
import time




class circularList(LinkedList):
            def __init__(self):
              super().__init__()
      

    # insertion method for the linked list
            def insert(self, data):
                newNode = Node(data)
                if(self.head):
                    current = self.head
                    while(current.next):
                        current = current.next
                    current.next = newNode
                else:
                    self.head = newNode
            
            # printing linked list 1
            def printLL(self):
                current = self.head
                while(current):
                    print(current.data)
                    current = current.next
                raise Exception(StopIteration)  
            # printing linked list 2
            def __str__(self):  
                output=""
                current = self.head    
                while(current):
                        output= output +str(current.data)
                        current = current.next
                return output


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