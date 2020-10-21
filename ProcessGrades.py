# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python

grade1 = int(input('Enter grade 1: '))
grade2 = int(input('Enter grade 2: '))
grade3 = int(input('Enter grade 3: '))
grade4 = int(input('Enter grade 4: '))
grades = grade1, grade2, grade3, grade4
print('You entered: ', grades)

high = grade1
if grade2 >= high:
    high = grade2
if grade3 >= high:
    high = grade3
if grade4 >= high:
    high = grade4
print('Highest grade: ', high)

low = grade1
if grade2 <= low:
    low = grade2
if grade3 <= low:
    low = grade3
if grade4 <= low:
    low = grade4
print('Lowest grade: ', low)
average = sum(grades) / len(grades)
print('Average grade: ', round(average, 2))



