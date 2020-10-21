# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

from Circle import Circle

circle1 = Circle()
print('Print radius:','\n','The radius is '+str(circle1.getRadius())+str('.'))
print('Print area:','\n','The area is '+str(round(circle1.getArea(),2))+str('.'))
print('Print perimeter:','\n','The perimeter is ' + str(round(circle1.getPerimeter(),2))+str('.'))

print('\n')


circle2 = Circle()
circle2.setRadius(10)
print('Set radius to 10 and print the object:','\n',str(circle2.toString())+str('.'))
print('Print area:','\n','The area is '+str(round(circle2.getArea(),2))+str('.'))
print('Print perimeter:','\n','The perimeter is ' + str(round(circle2.getPerimeter(),2))+str('.'))


