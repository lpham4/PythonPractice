# Class: 1321L
# Sec: 02
# Lab: Python
# Name: Ly Pham

import random

myArray = [[0]*4,[0]*4,[0]*4,[0]*4]
for row in range(len(myArray)):
    for column in range(len(myArray)):
        myArray[row][column] = random.randint(0,100)
print('Array Grades:')
for row in myArray:
    for column in row:
        print(column, end=' ')
    print()

def max(myArray):
    max = myArray[0][0]
    for row in range(len(myArray)):
        for column in range(len(myArray)):
            if myArray[row][column] > max:
                max = myArray[row][column]
    return max
  
def min(myArray):
    min = myArray[0][0]
    for row in range(len(myArray)):
        for column in range(len(myArray)):
            if myArray[row][column] < min:
                min = myArray[row][column]
    return min

def Avg(myArray):
    sum = 0
    for rows in range(len(myArray)):
        for columns in range(len(myArray)):
            sum += myArray[rows][columns]
    return sum/16
    

print('Highest grade:',max(myArray))
print('Lowest grade:',min(myArray))
print('Class average:',Avg(myArray))



