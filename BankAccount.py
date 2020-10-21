# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

import datetime
import calendar

class BankAccount:
    
    def __init__(self,ID=0,balance=0,annualInterestRate=0,dateCreated=datetime.datetime.today()):
        self.ID = ID
        self.balance = balance
        self.annualInterestRate = annualInterestRate
        self.dateCreated = dateCreated

    def setID(self,ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def setbalance(self,balance):
        self.balance = balance
    def getbalance(self):
        return self.balance

    def setannualInterestRate(self,annualInterestRate):
        self.annualInterestRate = annualInterestRate
    def getannualInterestRate(self):
        return self.anualInterestRate

    def getdateCreated(self):
        return self.dateCreated

    def getMonthlyInterestRate(self):
        return (self.annualInterestRate/12)
    def getMonthlyInterest(self):
        return ((self.annualInterestRate/12)*(self.balance)/100)

    def withdraw(self,withdraw):
        self.balance = self.balance - withdraw
    def deposit(self,deposit):
        self.balance = self.balance + deposit

    def toString(self):
        return ('Account ID: '+str(self.ID)+'\n'+str('Account Balance: '+str('$')+str(self.balance))
                +'\n'+str('Interest Rate: '+str(self.annualInterestRate)+str('%'))+'\n'
                +str('Monthly Interest: '+str('$')+str(self.getMonthlyInterest()))+'\n'
                +str('Date opened: '+str(self.dateCreated)))

    
    
