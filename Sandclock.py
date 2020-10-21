# Class: 1321L
# Sec: 02
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham
# Lab: Python


rows = 3
i = 0
j = 0
for i in range (9,0,-2):
    for j in range (0,rows):
        print(" ", end = "")
    for j in range (0,i):
        print("*", end = "")
    rows+= 1
    print()
rows = 6
i = 0
j = 0
for i in range (3,11,2):
    for j in range (0,rows):
        print(" ", end = "")
    for j in range (0,i):
        print("*", end = "")
    rows-= 1
    print()

