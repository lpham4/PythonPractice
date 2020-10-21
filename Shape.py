# Class: 1321L
# Sec: 02
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham
# Lab: Python

rows = 8
for line in range (1,16,2):
    for space in range (0,rows):
        print(" ", end = "")
    for star in range (0,line):
        print("*", end = "")
    rows-= 1
    print()
    
       
