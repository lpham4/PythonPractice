# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham


def isValid(rect):
    result = 0
    if rect > 30:
        result = True
        return result
    else:
        result = False
        return result

def area(area):
    result = 0
    result = width * height
    return result

def perimeter(perimeter):
    result = 0
    result = (width + height) * 2
    return result

width = int(input('Enter width: '))
height = int(input('Enter height: '))
print('Entered width:',width)
print('Entered height:', height)

rect = width + height

if isValid(rect):
    print('Area:', area(area))
    print('Perimeter:', perimeter(rect))
else:
    print('This is an invalid rectangle. Try again.')

    
