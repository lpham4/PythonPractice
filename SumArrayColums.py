# Class: 1321L
# Sec: 02
# Lab: Python
# Name: Ly Pham


myArray = [[0]*4, [0]*4, [0]*4]
for row in range(0,3):
    for column in range(0,4):
        myArray[row][column] = int(input('Enter a number: '))
for row in myArray:
    for column in row:
        print(column,end=' ')
    print()

def sumColumns(myArray):
    sumArray = [0]*4
    for column in range(0,4):
        for row in range(0,3):
            sumArray[column] += myArray[row][column]
    return sumArray

sumArray = sumColumns(myArray)
for row in range(len(sumArray)):
    print('Sum of column',row,'is',sumArray[row])

            

                        



