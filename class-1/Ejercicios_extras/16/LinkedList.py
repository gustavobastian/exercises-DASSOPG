#! /usr/bin/python3
import os
import signal
import time

# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
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

  # extend linked list
  def extend(self,lista2):
      current = lista2.head
      while(current.next):  
        self.insert(current.data)
        current = current.next

# Singly Linked List with insertion and print methods

"""handler for clean quit
"""
def handler():    
    print("saliendo en forma ordenada")
    exit(0)

if __name__ == "__main__":
    i=0
    j=10
    LL = LinkedList()
    LL2 = LinkedList()
   
    while i<10:
        i=i+1               
        LL.insert(i)
        LL2.insert(j)
        j=j-1 
    
    print(LL)
    print(LL2)
    print("extend")
    LL.extend(LL2)
    print(LL)