# Class: 1321
# Sec: 02
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham
# Lab: Python


num = int(input('Enter number between 20 and 60: '))
print('Entered value:', num)
if num >= 20 and num <= 60:
    count = 2
    sum = 0
    while count <= num:
        sum = sum + count
        count = count + 2
    print('Sum of all even numbers between 2 and the input is:', sum)
else:
    print('Invalid input.')
