# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

from array import *

size = int(input('Enter class size: '))
myArray = array('l',[0] * size)
for i in range(size):
    myArray[i] = int(input('Enter a score: '))
print('Entered scores: ',myArray.tolist())



def printGrades(myArray):
    for j in range(len(myArray)):
        if myArray[j] >= 90:
            print('Student',j,'score is',myArray[j],'and grade is A.')
        elif myArray[j] >= 80:
            print('Student',j,'score is',myArray[j],'and grade is B.')
        elif myArray[j] >= 70:
            print('Student',j,'score is',myArray[j],'and grade is C.')
        elif myArray[j] >= 60:
            print('Student',j,'score is',myArray[j],'and grade is D.')
        elif myArray[j] < 60:
            print('Student',j,'score is',myArray[j],'and grade is F.')


print(printGrades(myArray))
