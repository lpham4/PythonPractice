# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python

annual_income = int(input('Enter annual income: '))
print('Annual income: $' + str(annual_income))

if annual_income <= 50000:
    tax_brack = 5
    tax = annual_income * .05
    print('Tax bracket: ', (str(tax_brack) +'%'))
    print('Tax due amount: $' + str(tax))
if annual_income > 50000 and annual_income <= 200000:
    tax_brack = 10
    tax = (.05 * 50000) + ((annual_income - 50000) * .10)
    print('Tax bracket: ', (str(tax_brack) + '%'))
    print('Tax due amount: $' + str(tax))
if annual_income > 200000 and annual_income <= 400000:
    tax_brack = 15
    tax = (.05 * 50000) + (.1 * 150000) + ((annual_income - 200000) * .15)
    print('Tax bracket: ', (str(tax_brack) + '%'))
    print('Tax due amount: $' + str(tax))
if annual_income > 400000 and annual_income <= 900000:
    tax_brack = 25
    tax = (.05 * 50000) + (.1 * 150000) + (.15 * 200000) + ((annual_income - 400000) * .25) 
    print('Tax bracket: ', (str(tax_brack) + '%'))
    print('Tax due amount: $' + str(tax))
if annual_income > 900000:
    tax_brack = 35
    tax = (.05 * 50000) + (.1 * 150000) + (.15 * 200000) + (.25 * 400000) + ((annual_income - 900000) * .35)
    print('Tax bracket: ', (str(tax_brack) + '%'))
    print('Tax due amount: $' + str(tax))

                                                                                

    





