#! /usr/bin/python3
# some function that returns the year in roman numeral
from math import pi,sqrt,pow
import os

table1=[" ",
        "I",    
        "II",
        "III",
        "IV",
        "V",
        "VI",
        "VII",
        "VIII",
        "IX"
        ]

table2=[" ",
        "X",    
        "XX",
        "XXX",
        "XL",
        "L",
        "LX",
        "LXX",
        "LXXX",
        "XC"
            ]            

table3=[" ",
        "C",    
        "CC",
        "CCC",
        "CD",
        "D",
        "DC",
        "DCC",
        "DCCC",
        "CM"
            ]                        
table4=[" ",
        "M",    
        "MM",
        "MMM"        
            ]                        


def romanAge(x):
    output=""    
    value1=int(x/1000)    
    if(value1>3999) : 
        print("error")
        exit(0)
    else:    
        value2 = int((x%1000)/100)
        value3 = int((x%100)/10)
        value4 = int((x%10))
    print (table4[value1] + table3[value2] + table2[value3]+ table1[value4])

number=1
while (number!=0) :
    os.system('clear')
    number=int(input("Input year:"))
    if(number==0):exit(0)
    romanAge(number)

exit(0)