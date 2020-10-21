# Class: 1321:
# Sec: 02
# Lab: Python
# Name: Ly Pham

from array import *

size = 10
array = array('l',[0]*size)
for num in range(len(array)):
    array[num] = int(input('Enter an integer: '))

print('Entered integers: ',array.tolist())

def Count(array):
    myarray = dict();
    for num in array:
        if num in myarray:
            myarray[num] = myarray[num] + 1;
        else:
            myarray[num] = 1;
    return myarray

myarray=Count(array)
for num in myarray:
    print(num,'occurred',myarray[num],'times')
    
