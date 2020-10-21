# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python


x1 = int(input('Enter circle 1 center x: '))
y1 = int(input('Enter circle 1 center y: '))
center1 = x1,y1
radius1 = int(input('Enter circle 1 radius: '))

x2 = int(input('Enter circle 2 center x: '))
y2 = int(input('Enter circle 2 center y: '))
center2 = x2,y2
radius2 = int(input('Enter circle 2 radius: '))

print('Circle 1 center is: ', center1)
print('Circle 1 radius is: ', radius1)
print('Circle 2 center is: ', center2)
print('Circle 2 radius is: ', radius2)

import math

distance = ((x2 - x1)**2 + (y2 - y1)**2)
radii = radius1 + radius2
if math.sqrt(distance) > radii:
    print('Circle 2 is completely outside circle 1')
elif math.sqrt(distance) <= (radius1 - radius2):
    print('Circle 2 is completely inside circle 1')
else:
    print('Circle 2 is overlapping with circle 1')

