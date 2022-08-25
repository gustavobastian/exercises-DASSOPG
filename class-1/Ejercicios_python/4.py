#! /usr/bin/python3

def es_par(x):        
    if(isinstance(x, int)==False): return "No es entero"    
    elif (x % 2 == 0) and (x>1): return True
    elif x==1 or x==0 : return False
    else: return False

print("1 es par?: "+str(es_par(1)))
print("4 es par?: "+str(es_par(4)))
print("5 es par?: "+str(es_par(5)))
print("2.5 es par?: "+str(es_par(2.5)))
print("0 es par?: "+str(es_par(0)))
print("0.33 es par?: "+str(es_par(0.33)))