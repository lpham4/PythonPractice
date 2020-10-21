# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham


import random
def secretNum():
    return random.randint(1,20)


def guess():
    gues = int(input('Guess a number between 1 and 20: '))
    return gues

def eval(gues, num):
    if gues == num:
        return 'Correct'
    if gues > num:
        return 'Too high'
    if gues < num:
        return 'Too low'

flag = 'yes'
while flag == 'Yes' or flag == 'yes':
    gues = 0    
    num = secretNum()
    while gues != num:
        gues = guess()
        print(eval(gues,num))
    flag = input('Enter yes to guess again or no to stop: ')
    gues = 0

        

    

    
    
