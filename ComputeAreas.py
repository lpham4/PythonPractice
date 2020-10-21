# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham
# Lab: Python

import math
def squarearea(side):
    area = 0
    area = side * side
    return round(area,2)

def rectanglearea(rect):
    area = 0
    area = width * length
    return area

def circlearea(radius):
    area = 0
    area = math.pi * radius * radius
    return round(area,2)

def trianglearea(tri):
    area = 0
    area = .5 *(base * height)
    return round(area,2)


side= float(input('Square side: '))

width = float(input('Rectangle width: '))
length = float(input('Rectangle length: '))
rect = width * length

radius = float(input('Circle radius: '))

base= float(input('Triangle base: '))
height= float(input('Triangle height: '))
tri = base * height


print('Square area: ', squarearea(side))
print('Rectangle area: ', rectanglearea(rect))
print('Circle area: ', circlearea(radius))
print('Triangle area: ', trianglearea(tri))






