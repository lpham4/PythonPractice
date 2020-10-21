# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python

number = int(input('Enter number between 0 and 1000: '))

print('Entered number: ', number)

sum = 0

while number > 0:
    sum = sum + (int(number % 10))
    number = number / 10
print('Sum of digits: ', sum)
