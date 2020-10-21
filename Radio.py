# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

class Radio:
    def __init__(self,station=1,volume=1,on=False):
        self.station = station
        self.volume = volume
        self.on = on
    def getStation(self):
        return self.station
    def getVolume(self):
        return self.volume

    def turnOn(self,on):
        self.on = True
    def turnOff(self,on):
        self.on = False

    def stationUp(self,station):
        self.station = self.station + station
    def stationDown(self,station):
        self.station = self.station - station

    def volumeUp(self,volume):
        self.volume = self.volume + volume
    def volumeDown(self,volume):
        self.volume = self.volume - volume
          

    def toString(self):
        if self.on == True:
            return ('The radio station is '+ str(self.station) +' and the volume level is ' + str(self.volume) + str('.'))
        else:
            return ('The radio is off.')
