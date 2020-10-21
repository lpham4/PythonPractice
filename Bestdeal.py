# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python

small_weight = int(input('Small box weight: '))
small_price = int(input('Small box price: '))
large_weight = int(input('Large box weight: '))
large_price = int(input('Large box price: '))
small_total = (small_price / small_weight)
large_total = (large_price / large_weight)
if small_total < large_total:
    print('Judgment: The small box is a better deal')
elif large_total < small_total:
    print('Judgment: The large box is a a better deal')
else:
    print('Judgment: Both boxes are of the same value')   
