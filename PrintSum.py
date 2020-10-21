# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham
# Lab: Python

integer = int(input('Enter an integer between 1 and 100: '))
print('You entered:', integer)
if integer < 1 or integer > 100:
    print('Invalid input. Try again.')
else:
    count = 0
    sum = 0
    while count <= integer:
        sum += count
        count += 1
    print('Sum of values: ', sum)

    
    
    
 
