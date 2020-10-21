# Class: 1321L
# Sec: 02
# Lab: Python
# Name: Ly Pham

from array import *

size = 10
myArray = array('l',[0]*size)
for num in range(len(myArray)):
    myArray[num] = int(input('Enter an integer: '))

def getValues(myArray):
    distinct = set(myArray)
    return distinct

print('Original array: ',myArray.tolist())
print('Distinct array: ',getValues(myArray))
