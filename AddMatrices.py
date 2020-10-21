# Class: 1321L
# Sec: 02
# Lab: Python
# Name: Ly Pham

myArray1 = [[0]*3, [0]*3, [0]*3]
for row in range(0,3):
    for column in range(0,3):
        myArray1[row][column] = int(input('Enter a number: '))
print('Matrix A:')
for row in myArray1:
    for column in row:
        print(column,end=' ')
    print()
myArray2 = [[0]*3, [0]*3, [0]*3]
for row in range(0,3):
    for column in range(0,3):
        myArray2[row][column] = int(input('Enter a number: '))
print('Matrix B:')
for row in myArray2:
    for column in row:
        print(column,end=' ')
    print()

    
def Addition(myArray1,myArray2):
    sumArray = [0]*3,[0]*3,[0]*3
    for rows in range(0,3):
        for columns in range(0,3):
            sumArray[rows][columns] = myArray1[rows][columns]+myArray2[rows][columns]
    return sumArray
            


sumArray = Addition(myArray1,myArray2)
print('Matrix A+B:')
for row in sumArray:
    for column in row:
        print(column,end=' ')
    print()
