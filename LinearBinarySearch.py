# Class: 1321L
# Sec: 02
# Lab: Python
# Name: Ly Pham

from array import *
size = 6
myArray = array('l',[0]*size)
for num in range(len(myArray)):
    myArray[num] = int(input('Enter an integer: '))

def LinearSearch(myArray,target):
    for i in range(len(myArray)):
        if myArray[i] == target:
            return i+1
    return -1
def BinarySearch(myArray,target):
    i = 0
    first = 0
    last = len(myArray)-1
    found = False

    while first<=last and not found:
        i+=1
        midpoint = (first+last)//2
        if myArray[midpoint] == target:
            return i
        else:
            if target < myArray[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return -1

    

print('Array values: ',myArray.tolist())
target = int(input('Target value: '))
if LinearSearch(myArray,target) == -1:
    print('Linear search comparisons: Not found.')
    print('Binary search comparisons: Not found.')
else:
    print('Linear search comparisons: ',LinearSearch(myArray,target))
    print('Binary search comparisons: ',BinarySearch(myArray,target))


