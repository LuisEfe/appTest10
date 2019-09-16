
import os
fruits = ["Pineaple","apple","orange"]

os.system ("cls")
print ("The first fruit is: ", fruits[0])
print ("The last fruit is: ", fruits[2])

'''escriba un programa que reciba en una lista 10 n, ingresados desde consola'''

'''Create list'''

n = []
i = 1


while i<=10 :
        print ("Press number ",i,": ")
        x = int(input())
        n.append (x)
        i = i+1

'''Show list'''
i=0
while i < 10 :
    print ("The valor in the position ",i,"is: ",n[i])
    i = i+1