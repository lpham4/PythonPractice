# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

import math
class Circle:
    def __init__(self,radius=1,area=0,perimeter=0):
        self.radius = radius
        self.area = area
        self.perimeter = perimeter

    def getRadius(self):
        return self.radius

    def setRadius(self,radius):
        self.radius = radius

    def getArea(self):
        self.area = (self.radius ** 2) * math.pi
        return self.area

    def getPerimeter(self):
        self.perimeter = self.radius * 2 * math.pi
        return self.perimeter

    def toString(self):
        return ('The circle has radius '+ str(self.radius))


        
    
