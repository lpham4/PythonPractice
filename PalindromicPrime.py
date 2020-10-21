# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham
    
def isPrime(num):
    if num <= 1:
       return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
                return False
    return True

def isPalindrome(num):
    var = num
    rev = 0
    while var > 0:
        rev = (rev * 10) + var % 10
        var = var // 10
    return num == rev
    

count = 2
num = 2
while count <= 51:
    if isPrime(num):
        if isPalindrome(num):
            print(num, end= '\t')
            if count % 10 == 1:
                print()
            count += 1
    num += 1
        



