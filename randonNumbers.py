'''Random numbers'''

from random import randint,uniform,random

def z ():
    a = randint(0,101)
    return a 

print ("¿numbers?")
x = int(input())

n = []
i = 0

while i<= x  :
    n.append (z())
    i = i+1

'''Show list'''
i=0
while i < x :
    print (n[i])
    i = i+1

'''Show first valor'''
print ("first valor")
print (n[0])
 

'''Show last valor'''
print ("last valor")
i=0
while i<x :
    print (n[i])
    i = i+1

