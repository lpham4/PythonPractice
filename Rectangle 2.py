# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

class Rectangle:
    def __init__(self,height=1.0,width=1.0):
        self.width = width
        self.height = height

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)



