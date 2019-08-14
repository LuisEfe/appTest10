#randint = Generate random integer numbers
#Uniform =  Generate random float numbers

import os
from random import randint, uniform, random

def z ():
    a = randint(0,101)
    return a 
def r ():
    b = uniform(0,100)
    return b
os.system ("cls")
print ("The Z number is: ", z())
print ("The R number generate is: ", r())