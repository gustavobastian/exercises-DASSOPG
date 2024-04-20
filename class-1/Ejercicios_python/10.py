#! /usr/bin/python3
# getting all the ttys from the system
import os

list = {}
def myfun():
    cmd_out = os.popen('ls /dev/tty*').read()
    print(cmd_out)
    return True

myfun()