# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

from Radio import Radio
radio1 = Radio()
radio1.turnOn(True)
print('Turn radio on:','\n',str(radio1.toString()))

radio1.turnOn(True)
radio1.volumeUp(3)
print('Turn volume up by 3:','\n',str(radio1.toString()))

radio1.turnOn(True)
radio1.stationUp(5)
print('Move station up by 5:','\n',str(radio1.toString()))

radio1.turnOn(True)
radio1.volumeDown(1)
print('Turn volume down by 1:','\n',str(radio1.toString()))

radio1.turnOn(True)
radio1.stationUp(3)
print('Move station up by 3:','\n',str(radio1.toString()))

radio1.turnOff(True)
print('Turn radio off.','\n',str(radio1.toString()))

radio1.turnOff(True)
radio1.volumeUp(2)
print('Turn volume up by 2:','\n',str(radio1.toString()))

radio1.turnOff(True)
radio1.stationDown(2)
print('Turn station down by 2:','\n',str(radio1.toString()))

