# Dylan Rossman
# October 16, 2024
# P3HW1
# The program will display the employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay

employee_name = input('Enter employee\'s name:')
hours = float(input('Enter number of hours worked:'))
pay_rate = float(input('Enter employee\'s pay rate:'))

if hours > 40:
    overtime = hours - 40
else:
    overtime = 0
over_pay = overtime * pay_rate * 1.5
reg_pay = pay_rate * min(hours, 40)
gross_pay = over_pay + reg_pay

print('------------------------------')
print('Employee name:', employee_name)
print('\nHours Worked  Pay Rate   Overtime   Overtime Pay  Reghour Pay   Gross Pay')
print('---------------------------------------------------------------------------')
print(f'{hours:<13} {pay_rate:<10} {overtime:<10} {over_pay:<13.2f} {reg_pay:<13.2f} {gross_pay:}')

#  PRINT "Enter employee's name:"
#    READ employee_name
#
#    PRINT "Enter number of hours worked:"
#    READ hours
#
#    PRINT "Enter employee's pay rate:"
#    READ pay_rate
#
#    IF hours > 40 THEN
#        SET overtime = hours - 40
#    ELSE
#        SET overtime = 0
#    ENDIF
#
#    SET over_pay = overtime * pay_rate * 1.5
#    SET reg_pay = pay_rate * MIN(hours, 40)
#    SET gross_pay = over_pay + reg_pay
#
#    PRINT "------------------------------"
#    PRINT "Employee name:", employee_name
#    PRINT "Hours Worked  Pay Rate   Overtime   Overtime Pay  Reg Hour Pay   Gross Pay"
#    PRINT "---------------------------------------------------------------------------"
#    PRINT hours, pay_rate, overtime, over_pay, reg_pay, gross_pay
