# Class: 1321L
# Section: 02
# Term: Fall 2018
# Instructor: Professor Malcolm
# Name: Ly Pham
# Lab: Python

regular_fee = 15.00
regular_rate = .50
premium_fee = 25.00
premium_day_rate = .20
premium_night_rate = .10


account = int(input('Enter account number: '))
service = str(input('Enter service type: '))
print('Account number: ', account)
if service == 'r' or service == 'R':
    print('Service type: Regular')
    minutes = int(input('Total minutes: '))
    if minutes > 50:
        amount = (minutes - 50) * regular_rate + regular_fee
        print('Amount due: $' + str(amount))
    else:
        print('Amount due: $' + str(regular_fee))
elif service == 'p' or service == 'P':
    print('Service type: Premium')
    day_minutes = int(input('Daytime minutes: '))
    night_minutes = int(input('Nighttime minutes: '))
    if day_minutes > 50 and night_minutes > 100:
        day_amount = (day_minutes - 50) * premium_day_rate
        night_amount = (night_minutes - 100) * premium_night_rate
        premium_amount = day_amount + night_amount + premium_fee
        print('Amount due: $' + str(premium_amount))
    if day_minutes < 50 and night_minutes > 100:
        premium_amount = (night_minutes - 100) * premium_night_rate + premium_fee
        print('Amount due: $' + str(premium_amount))
    if day_minutes > 50 and night_minutes < 100:
        premium_amount = (day_minutes -50) * premium_day_rate + premium_fee
        print('Amount due: $' + str(premium_amount))
    if day_minutes < 50 and night_minutes < 100:
        premium_amount = premium_fee
        print('Amount due: $' + str(premium_amount))
  
  
                            
    

        




    



