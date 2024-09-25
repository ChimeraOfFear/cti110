# Dylan Rossman
# September 25, 2024
# P2Lab1
# The program will calculate the diameter, circumference, and area of a circle

print('What is the radius of the circle?',end=' ')
circle_radius = float(input())

diameter = circle_radius * 2
print('\nThe diameter of the circle is', diameter)

pi = 3.141592653589793
circumference = 2 * pi * circle_radius

print('\nThe circumference of the circle is %.2f' % circumference)

area = pi * (circle_radius ** 2)

print('\nThe area of the circle is %.3f' % area,)




