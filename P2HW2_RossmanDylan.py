#Dylan Rossman
#October 7, 2024
#P2HW2
#Create a python program that accepts grade inputs and outputs stats

grades = []

grade1 = float(input('Enter grade for Module 1: '))
grades.append(grade1)

grade2 = float(input('Enter grade for Module 2: '))
grades.append(grade2)

grade3 = float(input('Enter grade for Module 3: '))
grades.append(grade3)

grade4 = float(input('Enter grade for Module 4: '))
grades.append(grade4)

grade5 = float(input('Enter grade for Module 5: '))
grades.append(grade5)

grade6 = float(input('Enter grade for Module 6: '))
grades.append(grade6)

lowest_grade = min(grades)
highest_grade = max(grades)
sum_grades = sum(grades)
average_grade = sum_grades / len(grades)

print('\n------------Results-------------')
print('{:<18} {:.2f}'.format('Lowest grade:', lowest_grade))
print('{:<18} {:.2f}'.format('Highest grade:', highest_grade))
print('{:<18} {:.2f}'.format('Sum of grades:', sum_grades))
print('{:<18} {:.2f}'.format('Average grade:', average_grade))
print('--------------------------------')

# DECLARE grades AS LIST
#
#    PRINT "Enter grade for Module 1:"
#    INPUT grade1
#    APPEND grade1 TO grades
#
#    PRINT "Enter grade for Module 2:"
#    INPUT grade2
#    APPEND grade2 TO grades
#
#    PRINT "Enter grade for Module 3:"
#    INPUT grade3
#    APPEND grade3 TO grades
#
#    PRINT "Enter grade for Module 4:"
#    INPUT grade4
#    APPEND grade4 TO grades
#
#    PRINT "Enter grade for Module 5:"
#    INPUT grade5
#    APPEND grade5 TO grades
#
#    PRINT "Enter grade for Module 6:"
#    INPUT grade6
#    APPEND grade6 TO grades
#
#    SET lowest_grade TO MINIMUM OF grades
#    SET highest_grade TO MAXIMUM OF grades
#    SET sum_grades TO SUM OF grades
#    SET average_grade TO sum_grades DIVIDED BY LENGTH OF grades
#
#    PRINT "------------Results-------------"
#    PRINT "Lowest grade: ", lowest_grade
#    PRINT "Highest grade: ", highest_grade
#    PRINT "Sum of grades: ", sum_grades
#    PRINT "Average grade: ", average_grade
#    PRINT "--------------------------------"
