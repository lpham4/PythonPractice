# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

import random
from array import *
size = 5
myArray = array('l',[0]*size)
for nums in range(len(myArray)):
    myArray[nums] = random.randint(1,100)

def arrayMax(myArray):
    max = myArray[0]
    for num in range(len(myArray)):
        if myArray[num] > max:
            max = myArray[num]
    return max
          
def arrayMin(myArray):
    min = myArray[0]
    for num in range(len(myArray)):
        if myArray[num] < min:
            min = myArray[num]
    return min

def arraySquare(myArray):
    for num in range(len(myArray)):
        myArray[num] = myArray[num] ** 2
    return myArray
             
def arrayReverse(myArray):
    return myArray[::-1]
    
print('Original array:',myArray.tolist())
print('Max value:',arrayMax(myArray))
print('Min value:',arrayMin(myArray))
print('Squared array:',arraySquare(myArray))
print('Reversed array:',arrayReverse(myArray))


        




    
    
