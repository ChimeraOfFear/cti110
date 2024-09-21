#Dylan Rossman
#September 20, 2024
#P1HW1
#Create a python program using Idle to help the user calculate travel expenses 

print('This program calculates and displays travel expenses\n',)
print('Enter Budget:', end=' ')
budget = int(input())
print('\nEnter your travel destination:',end=' ')
destination = input()
print('\nHow much do you think you will spend on gas?',end=' ')
gas = int(input())
print('\nApproximately, how much will you need for accomodation/hotel?', end= ' ')
hotel = int(input())
print('\nLast, how much do you need for food?', end=' ')
food= int(input())
balance = budget - (gas + hotel + food)

print('\n------------Travel Expenses-------------',)
print('Location:', destination)
print('Initial Budget:', budget)
print('\nFuel:', gas)
print('Accomodation:', hotel)
print('Food:', food)
print('\nRemaining Balance:', balance)

#psuedocode
#Print "This program calculates and displays travel expenses" 
#Print "Enter Budget: "
#Input budget
#Print "Enter your travel destination: "
#Input destination
#Print "How much do you think you will spend on gas? "
#Input gas
#Print "Approximately, how much will you need for accommodation/hotel? "
#Input hotel
#Print "Last, how much do you need for food? "
#Input food
#balance = budget - (gas + hotel + food)

#Print "------------Travel Expenses-------------"
#Print "Location: ", destination
#Print "Initial Budget: ", budget
#Print "Fuel: ", gas
#Print "Accommodation: ", hotel
#Print "Food: ", food
#Print "Remaining Balance: ", balance
