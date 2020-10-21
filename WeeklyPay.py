# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python

hours = int(input('Enter hours: '))
print('You entered', hours, 'hours.')
parttime = hours * 10
fulltime = 40 * 10
overtime = (hours - 40) * 15
gross = (fulltime + overtime)

if hours == 40:
    print('Gross earning is $' + str(fulltime))
elif hours < 40:
    print('Gross earning is $' + str(parttime))
else:
    print('Gross earning is $' + str(gross))
