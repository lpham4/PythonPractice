# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

class Stock:
    def __init__(self,name="",symbol="",closingPrice=0,currentPrice=0):
        self.name = name
        self.symbol = symbol
        self.closingPrice = closingPrice
        self.currentPrice = currentPrice 

    def getName(self):
        return self.name
    
    def getSymbol(self):
        return self.symbol

    def setClosingPrice(self):
        return self.closingPrice

    def setCurrentPrice(self):
        return self.currentPrice

    def getChangePercent(self):
        return round(((self.currentPrice-self.closingPrice)/self.currentPrice*100),0)

    def __str__(self):
        return(self.name+" stock's closing price is $"+str(self.currentPrice))

    
        



