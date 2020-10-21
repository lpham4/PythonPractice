# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

from array import *
size = int(input('Enter array size: '))
myArray1 = array('l',[0] * size)
myArray2 = array('l',[0] * size)
for num in range(size):
    myArray1[num] = int(input('Enter a number: '))
for num in range(size):
    myArray2[num] = int(input('Enter a number: '))


def Compare(myArray1,myArray2):
    for nums in range(len(myArray1)):
        if myArray1[num] != myArray2[num]:
            return 'Judgment: The arrays are not identical.'
        else:
            return 'Judgment: The arrays are identical.'
 

print('Array 1: ',myArray1.tolist())
print('Array 2: ',myArray2.tolist())

print(Compare(myArray1,myArray2))

   
