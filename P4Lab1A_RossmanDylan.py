# Dylan Rossman
# October 26, 2024
# P4Lab1A
# The program will draw a square and a triangle

import turtle

turtle.shape("turtle")

for i in [0,1,2,3]:
    turtle.forward(50)
    turtle.right(90)

for i in [0,1,2]:
    turtle.forward(50)
    turtle.left(120)

turtle.exitonclick()
