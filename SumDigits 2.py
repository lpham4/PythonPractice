# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham



def sumDigits(num):
    sum = 0
    while num > 0:
        sum = sum + (int(num % 10))
        num = num / 10
    return sum

num = int(input('Enter an integer: '))
print('Sum of digits',+sumDigits(num))




