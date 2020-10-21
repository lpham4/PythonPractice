# Class: 1321L
# Sec: 02
# Lab: Python
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham

from Counter import Counter
from random import randint

heads = Counter()
tails = Counter()

for i in range(100):
    if randint(0,1) == 0:
        heads.increment()
    else:
        tails.increment()

print('Number of heads: '+str(heads.getValue()))
print('Number of tails: '+str(tails.getValue()))
