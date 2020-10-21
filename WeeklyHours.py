# Class: 1321L
# Sec: 02
# Lab: Python
# Name: Ly Pham

from array import *
import random

myArray = [[0]*7,[0]*7,[0]*7]
for row in range(len(myArray)):
    for column in range(len(myArray)):
        myArray[row][column]= random.randint(0,10)
print('Employees Data:')
print('M  T  W  Th  F  Sa  Su')
print('-----------------------')
for row in myArray:
    for column in row:
        print(column,end='  ')
    print()

def addHours(myArray):
    sumArray = [0]*3
    for column in range(len(myArray)):
        for row in range(len(myArray)):
            sumArray[row] += myArray[row][column]
    return sumArray
print('-----------------------')
print('Employee #:''   ''Weekly Hours:')
sumArray = addHours(myArray)
for column in range(len(myArray)):
    print((column+1),'           ',sumArray[column])
                    
    
    
