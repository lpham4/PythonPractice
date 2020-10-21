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
        print(column, end=' ')
    print()

def locateLargest(myArray):
    largestArray = [0]*2
    max1 = myArray[0][0]
    for row in range(0,3):
        for column in range(0,4):
            if myArray[row][column] > max1:
                max1 = myArray[row][column]
                largestArray[0] = row
                largestArray[1] = column
    return largestArray

largest= locateLargest(myArray)
print('First largest value is located at row',largest[0],'and column is',largest[1])

                      
    
