#Dylan Rossman
#September 25, 2024
#P2Lab1
#create a dictionary that gives info about cars

car = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

keys = car.keys()

print("Available vehicles:", list(keys))

car_input = input("Enter a vehicle to see it\'s mpg: ")

mpg = car[car_input]
print(f"The {car_input} gets {mpg} mpg.")

miles = float(input(f"How many miles will you drive the {car_input}? "))

gallons_needed = miles / mpg

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_input} {miles} miles.")

