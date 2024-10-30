#Dylan Rossman
#October 29, 2024
#P4HW1
#Create a python program that accepts grade inputs and outputs stats

grades = []
num=1
amount = int(input('How many scores do you want to enter? '))
for i in range(amount):
    while True:
        grade = float(input(f'Enter grade for Module {num}: '))
        if grade < 0 or 100 < grade:
            print('\nINVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            print(f'Enter score #{num} again')
        else:
            grades.append(grade)
            num+=1
            break


lowest_grade = min(grades)
new_grades = [grade for grade in grades if grade != lowest_grade]
average_grade = sum(new_grades) / len(new_grades)

if average_grade >= 90:
    letter_grade = 'A'
elif average_grade >= 80:
    letter_grade = 'B'
elif average_grade >= 70:
    letter_grade = 'C'
elif average_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print('\n------------Results-------------')
print(f'Lowest Score:', lowest_grade)
print(f'Modified List:', new_grades)
print(f'Scores Average:', average_grade)
print(f'Grade:', letter_grade)
print('--------------------------------')

#DECLARE grades as an empty list
#DECLARE num as 1
#PRINT How many scores do you want to enter
#
#FOR i FROM 0 TO amount - 1 DO
#    WHILE True DO
#        PRINT Enter grade for module
#        STORE the input in grade
#
#        IF grade is less than 0 OR grade is greater than 100 THEN
#            PRINT "INVALID Score entered!!!!"
#            PRINT "Score should be between 0 and 100"
#            PRINT "Enter score for Module num again"
#        ELSE
#            APPEND grade to grades
#            INCREMENT num by 1
#            BREAK the loop
#
#END FOR
#
#SET lowest_grade to the minimum value in grades
#CREATE new_grades as a list of grades excluding lowest_grade
#
#IF new_grades is not empty THEN
#    SET average_grade to the sum of new_grades divided by the length of new_grades
#
#    IF average_grade >= 90 THEN
#        SET letter_grade to 'A'
#    ELSE IF average_grade >= 80 THEN
#        SET letter_grade to 'B'
#    ELSE IF average_grade >= 70 THEN
#        SET letter_grade to 'C'
#    ELSE IF average_grade >= 60 THEN
#        SET letter_grade to 'D'
#    ELSE
#        SET letter_grade to 'F'
#    
#    PRINT "------------Results-------------"
#    PRINT "Lowest Score:", lowest_grade
#    PRINT "Modified List:", new_grades
#    PRINT "Scores Average:", average_grade
#    PRINT "Grade:", letter_grade
#    PRINT "--------------------------------"
