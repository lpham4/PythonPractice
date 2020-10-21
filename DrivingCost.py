# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python

distance = float(input('Distance traveled (miles): '))

mpg = int(input('Miles per gallon (miles): '))

ppg = float(input('Price per gallon (dollars): '))

cost = ((distance / mpg) * ppg)

print('Trip cost (dollars):', '%.2f' % cost)
