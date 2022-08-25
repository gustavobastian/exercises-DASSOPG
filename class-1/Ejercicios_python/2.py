#! /usr/bin/python3

mylist= []

print("id:"+str(id(mylist)))
print("type:"+str(type(mylist)))
print("value:"+str((mylist)))

print("****adding number*******")

mylist.append(2)
print("id:"+str(id(mylist)))
print("type:"+str(type(mylist)))
print("value:"+str((mylist)))

print("Conclusion: Solo se modificó el valor de la misma,\n tanto el id como el tipo se mantuvieron")