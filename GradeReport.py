# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python

grade = int(input('You entered '))

if grade >= 100:
    print('That grade is a perfect score. Well done.')
elif grade >= 90:
    print('That grade is well above average. Excellent work.')
elif grade >= 80:
    print('That grade is above average. Nice job.')
elif grade >= 70:
    print('That grade is average work.')
elif grade >= 60:
    print('That grade is not good, you should seek help!')
else:
    print('That grade is not passing.')
