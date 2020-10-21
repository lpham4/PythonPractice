# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

class Counter:
    def __init__(self,counter=0):
        self.counter = counter

    def increment(self):
        self.counter = self.counter + 1

    def getValue(self):
        return self.counter
    
    
