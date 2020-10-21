# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python


day = int(input("Enter today's day: "))
days = int(input('Enter days until meeting: '))

if day == 0:
    print('Today is Sunday')
elif day == 1:
    print('Today is Monday')
elif day == 2:
    print('Today is Tuesday')
elif day == 3:
    print('Today is Wednesday')
elif day == 4:
    print('Today is Thursday')
elif day == 5:
    print('Today is Friday')
elif day == 6:
    print('Today is Saturday')
print('Days to the meeting is', days, 'days')

meeting = (day + days) % 7
if meeting == 0:
    print('Meeting day is Sunday')
elif meeting == 1:
    print('Meeting day is Monday')
elif meeting == 2:
    print('Meeting day is Tuesday')
elif meeting  == 3:
    print('Meeting day is Wednesday')
elif meeting == 4:
    print('Meeting day is Thursday')
elif meeting == 5:
    print('Meeting day is Friday')
elif meeting == 6:
    print('Meeting day is Saturday')

    









