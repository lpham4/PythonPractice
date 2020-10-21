# Class: 1321L
# Sec: 02
# Lab: Python
# Name: Ly Pham

from array import *
import random

def BubbleSort(unsorted):
    count = 0
    for i in range(len(unsorted)):
        for j in range(0,len(unsorted)-i-1):
            if unsorted[j] > unsorted[j+1]:
                temp = unsorted[j]
                unsorted[j] = unsorted[j+1]
                unsorted[j+1] = temp
                count += 1
    return count
        

def InsertionSort(unsorted):
    count = 0
    for i in range(1,len(unsorted)):
        current = unsorted[i]
        position = i
        while position > 0 and unsorted[position-1] > current:
            unsorted[position] = unsorted[position-1]
            position = position-1
            count += 1
    unsorted[position] = current
    return count

def SelectionSort(unsorted):
    count = 0
    for i in range(len(unsorted)):
        positionOfMin = i
        for j in range(i+1,len(unsorted)):
            if unsorted[positionOfMin] > unsorted[j]:
                positionOfMin = j
        if positionOfMin != i:
            temp = unsorted[i]
            unsorted[i] = unsorted[positionOfMin]
            unsorted[positionOfMin] = temp
            count += 1
    return count


    
size = 50
myArray1 = array('l',[0]*size)
for nums in range(len(myArray1)):
    myArray1[nums] = random.randint(0,100)
swaps = BubbleSort(myArray1)
print('Bubble sorted values:',myArray1.tolist())
print('Bubble sort swaps:',swaps)

print('\n')


size = 50
myArray2 = array('l',[0]*size)
for nums in range(len(myArray2)):
    myArray2[nums] = random.randint(0,100)  
swaps = InsertionSort(myArray2)
print('Insertion sorted values:',myArray2.tolist())
print('Insertion sort swaps:',swaps)

print('\n')

size = 50
myArray3 = array('l',[0]*size)
for nums in range(len(myArray3)):
    myArray3[nums] = random.randint(0,100)
swaps = SelectionSort(myArray3)
print('Selection sorted values:',myArray3.tolist())
print('Selection sort swaps:',swaps)
    
