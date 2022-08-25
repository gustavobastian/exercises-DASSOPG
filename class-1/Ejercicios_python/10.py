#! /usr/bin/python3
# getting all the ttys from the system
import os

list = {}
def myfun():
    cmdOut = os.popen('ls /dev/tty*').read()
    print(cmdOut)
    return True

myfun()