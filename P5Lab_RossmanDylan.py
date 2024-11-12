# Dylan Rossman
# November 11, 2024
# P5Lab
# The program will tell you what your change is
import random

money = round(random.uniform(0.01, 100.00), 2)
print(f"You owe ${money:.2f}")

paid = float(input("How much cash will you put in the self-checkout? $"))

change = paid - money
if change < 0:
    print("Sorry, that's not enough money!")
else:
    print(f"Your change is: ${change:.2f}")

    def money_function(amount):
        dollar_math = 100
        quarter_math = 25
        dime_math = 10
        nickel_math = 5
        penny_math = 1

        cents = int(amount * 100)

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

    money_function(change)
