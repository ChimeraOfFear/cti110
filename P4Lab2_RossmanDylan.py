# Dylan Rossman
# October 27, 2024
# P4Lab2
# The program is a multiplication table that can accept inputs

while True:
    integer = int(input('Enter an integer:'))
    if integer <0:
       print("This program does not handle negative numbers")
       run_again = input('Do you want to run the program again? (yes/no): ')
    else:
        x=0
        for i in [0,1,2,3,4,5,6,7,8,9,10,11]:
             x+=1
             answer = (integer * x)
             print(integer ,'*', x, '=', answer )
       
        run_again = input('Do you want to run the program again? (yes/no): ')
        if run_again.lower() != 'yes':
            print('Exiting program...')
            break
    
