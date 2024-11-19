# Dylan Rossman
# November 19, 2024
# P5HW
# The program will display a working math quiz

import random

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def display_menu():
    print("\nWelcome to Math Quiz")
    print("\nMain Menu")
    print("----------------------")
    print("1.Adding Random Numbers")
    print("2.Subtracting Random Numbers")
    print("3.Exit")

display_menu()

while True:
    menu_option = input("\nPlease choose one of the menu options:")

    if menu_option == "1":
        
        num1 = random.randint(1, 100)  
        num2 = random.randint(1, 100)
        add_answer = add(num1, num2)
        guess_count = 0
        print (" ",num1)
        print ("+",num2)
        print("\nEnter answer.")
        while True:
            user_input = int(input())
            guess_count += 1
            if user_input > add_answer:
                    print("\nSorry, guess is too high.")
                    print("Try again: ", end='')
            elif add_answer > user_input: 
                    print("\nSorry, guess is too low.")
                    print("Try again: ", end='')
            else:
                    print("\nCongratulations!!! Your answer is correct.")
                    print("Number of Guesses:",guess_count)
                    display_menu()
                    break
            
        
    elif menu_option == "2":
        
        num1 = random.randint(1, 100)  
        num2 = random.randint(1, 100)
        sub_answer = sub(num1, num2)
        guess_count = 0
        print (" ",num1)
        print ("-",num2)
        print("\nEnter answer.")
        while True:
            user_input = int(input())
            guess_count += 1
            if user_input > sub_answer:
                    print("\nSorry, guess is too high.")
                    print("Try again: ", end='')
            elif sub_answer > user_input: 
                    print("\nSorry, guess is too low.")
                    print("Try again: ", end='')
            else:
                    print("\nCongratulations!!! Your answer is correct.")
                    print("Number of Guesses:",guess_count)
                    display_menu()
                    break

    elif menu_option == "3":
        print("\nThank you for playing... \nBye!!")
        break
        
    else:
        print("Invalid input! Please choose 1, 2, or 3.")
        continue
        
        
        




        


