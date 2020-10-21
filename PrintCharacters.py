# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham



def printChars(ch1,ch2):
    print('Start character: ', ch1)
    print('end character: ', ch2)
    count = ord(ch1)
    i = 0
    while count <= ord(ch2):
        if i == 5:
            print()
            print(chr(count),end='')
            i = 1
        else:
            print(chr(count),end='')
            i = i + 1
        count = count + 1



ch1 = input('Enter start character: ')
ch2 = input('Enter end character: ')
while ch2 < ch1:
    print('Start and end characters are out of order. Try again.')
    ch1 = input('Enter start character: ')
    ch2 = input('Enter end character: ')
print(printChars(ch1,ch2))

