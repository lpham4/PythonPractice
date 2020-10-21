# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python

x = int(input('X-coordinate is: '))
y = int(input('Y-coordinate is: '))
point = x, y

if x == 0 and y == 0:
    print(point, 'is the origin point.')
elif x == 0:
    print(point, 'is on the y-axis.')
elif y == 0:
    print(point, 'is on the x-axis.')
if x > 0 and y > 0:
    print(point, 'is in the first quadrant.')
if x < 0 and y > 0:
    print(point, 'is in the second quadrant.')
if x < 0 and y < 0:
    print(point, 'is in the third quadrant.')
if x > 0 and y < 0:
    print(point, 'is in the fourth quadrant.')










