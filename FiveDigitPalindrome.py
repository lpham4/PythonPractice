# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python

number = int(input('Enter five digit number: '))
num = number
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10 
if num == reverse:
    print('Valid 5-digit palindrome')
else:
    print('Invalid 5-digit palindrome')
    
    
