# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

def feetToMeter(feet):
    meter = feet * 0.305
    return meter

def meterToFeet(meter):
    feet = meter * 3.279
    return feet

print('Feet \t Meter')
for feet in range (1,21,1):
    print(feet, '\t', round(feetToMeter(feet),2))
print('\t')
print('Meter \t Meter')
for meter in range (1,21,1):
    print(meter, '\t', round(meterToFeet(meter),2))
