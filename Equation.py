# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

import math
class Equation:
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def geta(self):
        return self.a

    def getb(self):
        return self.b

    def getc(self):
        return self.c

    def getDiscriminant(self):
        return ((self.b**2)-(4*self.a*self.c))

    def getRoot1(self):
        d = self.getDiscriminant()
        return (-self.b+math.sqrt(d))/(2*self.a)
     
    def getRoot2(self):
        d = self.getDiscriminant()
        return (-self.b-math.sqrt(d))/(2*self.a)
      
    
