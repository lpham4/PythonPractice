# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

from Rectangle import Rectangle

rec1 = Rectangle()
print('First Object:')
print('Height: ' ,rec1.getHeight(),'unit')
print('Width: ' ,rec1.getWidth(),'unit')
print('Area: ',rec1.getArea(),'unit')
print('Perimeter: ',rec1.getPerimeter(),'units')

print('\n')

rec2 = Rectangle(5,6)
print('Second Object:')
print('Height: ',rec2.getHeight(),'units')
print('Width: ',rec2.getWidth(),'units')
print('Area: ',rec2.getArea(),'units')
print('Perimeter: ',rec2.getPerimeter(),'units')
