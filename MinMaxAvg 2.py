# Class: 1321L
# Secion: 02
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham
# Lab: Python

def max(x,y,z):
    result = 0
    if x > y and x > z:
        result = x
    elif y > x and y > z:
        result = y
    elif z > x and z > y :
        result = z
    return result

def min(x,y,z):
    result = x
    if y < result:
        result = y
    if z < result:
        result = z
    return result

def avg(x,y,z):
    average = (x+y+z) / 3
    return round(average,2)

x = int(input('Enter first integer: '))
y = int(input('Enter second integer: '))
z = int(input('Enter third integer: '))
print('You entered:',(str(x)+','),(str(y)+','),z)

print('Max value: ', max(x,y,z))
print('Min value: ', min(x,y,z))
print('Average value: ', avg(x,y,z))



   



