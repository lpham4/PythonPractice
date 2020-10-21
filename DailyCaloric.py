# Class: 1321L
# Sec: 02
# Term: Fall 2018
# Instructor: Malcolm
# Name: Ly Pham
# Lab: Python

height = int(input('Enter height in inches: '))
weight = int(input('Enter weight in pounds: '))
gender = str(input('Enter gender: '))
age = int(input('Enter age: '))
print("1.You dont't exercise.")
print("2.You engage in light exercise 1-3 days a week.")
print('3.You exercise moderate 3-5 days a week.')
print('4.You exercise intensely 6-7 days a week.')
print('5.You exercise intensely 6-7 days a week and have a physically active job.')
exercise = int(input('Choose level of exercise: '))

while gender == str('female') or gender == str('Female'):
    female_bmr = (655 + (4.35 * weight) + (4.7 * height) - (4.7 * age))
    if exercise == 1:
        dc = female_bmr * 1.2
    if exercise == 2:
        dc = female_bmr * 1.375
    if exercise == 3:
        dc = female_bmr * 1.55
    if exercise == 4:
        dc = female_bmr * 1.725
    if exercise == 5:
        dc = female_bmr * 1.9
    print(str(gender)+',', str(height)+'"'',', str(weight)+' lbs,', 'age '+str(age)+',', 'BMR = '+str(round(female_bmr,2))+',','Exercise '+str(exercise)+',','DCA: '+str(round(dc,2)))
    break
while gender == str('male') or gender == str('Male'):
    bmr = (66 + (6.23 * weight) + (12.7 * height) - (6.8 * age))
    if exercise == 1:
        dc = bmr * 1.2
    if exercise == 2:
        dc = bmr * 1.375
    if exercise == 3:
        dc = bmr * 1.55
    if exercise == 4:
        dc = bmr * 1.725
    if exercise == 5:
        dc = bmr * 1.9
    print(str(gender)+',', str(height)+'"'',',str(weight)+' lbs,', 'age '+str(age)+',','BMR = '+str(round(bmr,2))+',','Exercise '+str(exercise)+',','DCA: '+str(round(dc,2)))
    break


