# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

from Equation import Equation


a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
myObject=Equation(a,b,c)
print('a = '+str(myObject.geta()))
print('b = '+str(myObject.getb()))
print('c = '+str(myObject.getc()))
if myObject.getDiscriminant() < 0:
    print('Root 1 is undefined.')
else:
    print('Root 1 = '+str(myObject.getRoot1()))
if myObject.getDiscriminant() < 0:
    print('Root 2 is undefined.')
else:
    print('Root 2 = '+str(myObject.getRoot2()))

