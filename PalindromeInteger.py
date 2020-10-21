# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham
# Lab: Python

def reversednum(num):
    reversednum = 0
    digit = 0

    while num > 0:
        digit = num % 10
        reversednum = ((reversednum * 10) + digit)
        num = num // 10
    return reversednum

def judgment(num):
    result = ""
    rev = reversednum(num)
    if num == rev:
        result = 'Palindrome'
    else:
        result = 'Not palindrome'
    return result  

num = int(input('Enter an integer: '))
print('Entered value:', num)
print('Judgment: ', judgment(num)) 



