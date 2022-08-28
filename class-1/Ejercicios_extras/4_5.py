#! /usr/bin/python3
# some function that works with days
from math import pi,sqrt,pow
import os

tableDays=[31,
           28,
           31,
           30,
           31,
           30,
           31,
           31,
           30,
           31,
           30,
           31]


#a
def bisiesto(x):        
    if (x%4==0 and x%100!=0) or (x%400==0): return True
    else: return False

#b
def day_per_month(x):
    return tableDays[x]

## parameter in form "dd/mm/yy"
def date_valid(date):
    value=splitDate(date)
    day=int(value[0])
    month=int(value[1])
    year=int(value[2])
#check limits
    if ((day<0) or (day>31) or (month<0) or (month>12)): 
        print("invalid date")
        return False    
    elif (day<=tableDays[month-1]):
        print("valid Date")
    elif (day==29) and (month==2) and (bisiesto(year)==True):
        print("valid Date")    
    else :
        print("invalid Date")   

## parameter in form "dd/mm/yy"
def splitDate(date):
    date = date.split('/')        
    return date

## parameter in form "dd/mm/yy"
def daysLastMonth(date):
    if(date_valid(date)==False) : return "error"
    value=splitDate(date)
    day=int(value[0])
    month=int(value[1])
    year=int(value[2])
    days=tableDays[month-1]-day
    if (( bisiesto(year)== True) and month==2) : days+=1
    return days


## parameter in form "dd/mm/yy"
def daysLastYear(date):
    if(date_valid(date)==False) : return "error"
    value=splitDate(date)
    day=int(value[0])
    month=int(value[1])
    year=int(value[2])
    days=tableDays[month-1]-day
    if(month==12):return days
    else:
        for i in range(month, 12):
            days+= tableDays[i-1]
        if (( bisiesto(year)== True) and ((month<2) or ((month==2)and(day<29)) )): days+=1
    return days

## parameter in form "dd/mm/yy"
def countingDays(date):
    if(date_valid(date)==False) : return "error"
    value=splitDate(date)
    day=int(value[0])
    month=int(value[1])
    year=int(value[2])
    days=day
    if(month==1):return days
    else:
        for i in range(1, month):
            days+= tableDays[i-1]
        if (( bisiesto(year)== True) and ((month>2) )): days+=1
    return days

#date comparison, returns true if date1 happens after date2, false in the other case
def  date_comparison(date1,date2):
    if(date_valid(date1)==False) : return "error"
    if(date_valid(date2)==False) : return "error"
    value1=splitDate(date1)
    value2=splitDate(date2)
    
    if(value1[2]==value2[2]):
        if(value1[1]==value2[1]):    
            if (value1[0]>value2[0]):return True
            else : return False
        elif (value1[1]>value2[1]):return True
        else :return False   
    elif (value1[2]>value2[2]):return True            
    else: False

# counting days between dates
def counting_days_between(value1, value2):
    isOk= date_comparison(value1,value2)

    # in date 1 always will be the earliest date
    if(isOk==False): 
        date1=(value1)
        date2=(value2)
    else:
        date1=(value2)
        date2=(value1)

    #splitting the dates for checking years
    date1_s=splitDate(date1)
    date2_s=splitDate(date2)
    
    days=0
    if(date1_s[2]==date2_s[2]):
        if(date1_s[1]==date2_s[1]):
            days=int(date2_s[0])-int(date1_s[0])
        else:
            if(int(date1_s[1])<int(date2_s[1])):                
                days=int(date2_s[0])+daysLastMonth(date1)
                for i in range(int(date1_s[1]),int(date2_s[1])-1):
                    days+=tableDays[i-1]

                if ((bisiesto(int(date1_s[2]))==True) and (int(date1_s[1])<3)) and (int(date2_s[1])>2):                        
                        print(bisiesto(int(date1_s[2])))
                        days+=1     
            else:## as we order the dates previously, we do not need to worry abour this case                
                days=0        
    else:        
        days=countingDays(date1)+daysLastYear(date2)        
        for i in range(int(date2_s[2])+1,int(date1_s[2])):                    
                    days+=365
                    if(bisiesto(i)==True):                         
                        print(i)
                        days+=1


        

    return days    
    


number=1
while (number!=0):
    os.system('clear')
    #number=int(input("Numero: "))
    #if(number !=0): print(bisiesto(number))
    #if(number !=0): 
    #    if (number<13) and (number >0):print(day_per_month(number-1))
    #else : exit(0)
    date1=(input("fecha1  day/month/year : "))
    date2=(input("fecha2  day/month/year : "))
    print(bisiesto(1999))
    #print(date_valid(date))
    #print(daysLastMonth(date))
    #print(daysLastYear(date))
    #print(countingDays(date))
    #print(date_comparison(date,date2))
    #print(date_comparison(date2,date))
    print("Days between dates:")
    print(counting_days_between(date1,date2))
    
    print("press enter to continue(q to quit) ")
    n=input(">")
    if (n=='q'): exit(0)