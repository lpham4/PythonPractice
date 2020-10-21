# Class: 1321:
# Sec: 02
# Lab: Python
# Name: Ly Pham

from array import *

size = 10
myArray = array('i',[0]*size)
for num in range(len(myArray)):
    myArray[num] = int(input('Enter an integer: '))

def findIndex(myArray):
    max = myArray[0]
    for num in range(len(myArray)):
        if myArray[num] > max:
            max = myArray[num]
    return max    




print('Entered integers: ',myArray.tolist())
max1 = findIndex(myArray)
print('Index of largest value is ',myArray.index(max1))

