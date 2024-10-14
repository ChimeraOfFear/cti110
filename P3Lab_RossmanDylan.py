# Dylan Rossman
# October 14, 2024
# P3Lab
# The program will display the input number as money

money = float(input('Enter the amount of money as a float: $'))
dollar_math = 100
quarter_math = 25
dime_math = 10
nickel_math = 5
penny_math = 1

cents = int(money * 100)

dollars = cents // dollar_math
cents -= dollars * dollar_math

quarters = cents // quarter_math
cents -= quarters * quarter_math

dimes = cents // dime_math
cents -= dimes * dime_math

nickels = cents // nickel_math
cents -= nickels * nickel_math

pennies = cents // penny_math

coins = False

if dollars > 0:
    print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    coins = True
if quarters > 0:
    print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    coins = True
if dimes > 0:
    print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    coins = True
if nickels > 0:
    print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    coins = True
if pennies > 0:
    print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")
    coins = True
if not coins:
    print('No change')
