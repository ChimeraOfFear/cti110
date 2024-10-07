# Dylan Rossman
# October 7, 2024
# P2HW1
# The program will calculate and display travel expenses

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

print('\n------------Travel Expenses-------------')
print('{:<18} {}'.format('Location:', destination))  
print('{:<18} ${:.2f}'.format('Initial Budget:', budget))  
print('{:<18} ${:.2f}'.format('Fuel:', gas))  
print('{:<18} ${:.2f}'.format('Accommodation:', hotel))  
print('{:<18} ${:.2f}'.format('Food:', food))  
print('----------------------------------------')
print('{:<18} ${:.2f}'.format('Remaining Balance:', balance)) 
