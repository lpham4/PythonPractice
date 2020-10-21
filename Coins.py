# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python


quarters = int(input('Enter number of quarters: '))
dimes = int(input('Enter number of dimes: '))
nickels = int(input('Enter number of nickels: '))
pennies = int(input('Enter number of pennies: '))
print('You entered', quarters, 'quarters')
print('You entered', dimes, 'dimes')
print('You entered', nickels, 'nickels')
print('You entered', pennies, 'pennies')
dollars = ((.25*quarters) + (.10*dimes) + (.05*nickels) + (.01*pennies) % 100)/1
cents = ((.25*quarters) + (.10*dimes) + (.05*nickels) + (.01*pennies) % 10)
print('Your total is',int(dollars), 'dollars', int((cents%1)*100), 'cents',)




