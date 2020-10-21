# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

def displaySums(num):
    print('i\tSum(i)')
    sum = 0
    for i in range (1,num+1,1):
        sum = sum + (i/(i+1))
        print(i,'\t',round(sum,4))



num = int(input('Enter an integer: '))
print(displaySums(num))

