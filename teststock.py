# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

from Stock import Stock

stock1 = Stock('Google','GOG',134.67,131.98)
print(stock1.getName()+' stock:')
print('Symbol: ',stock1.getSymbol())
print('Closing price: ',stock1.setClosingPrice())
print('Current price: ',stock1.setCurrentPrice())
print('Change percent: '+str(stock1.getChangePercent())+"%")
print(stock1)


print('\n')

stock2 = Stock('Microsoft','MSF',156.52,161.22)
print(stock2.getName()+' stock:')
print('Symbol: ',stock2.getSymbol())
print('Closing price: ',stock2.setClosingPrice())
print('Current price: ',stock2.setCurrentPrice())
print('Change percent: '+str(stock2.getChangePercent())+"%")
print(stock2)



