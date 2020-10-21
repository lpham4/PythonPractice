# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

from BankAccount import BankAccount

myObject = BankAccount()
myObject.setID(123456)
myObject.setbalance(10000)
myObject.withdraw(3500)
myObject.deposit(500)
myObject.setannualInterestRate(2.50)
print(myObject.toString())

