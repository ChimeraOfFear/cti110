# Dylan Rossman
# October 26, 2024
# P4Lab1B
# The program will draw a D and an R

import turtle

turtle.shape("turtle")
turtle.color("purple")
turtle.speed(30)
turtle.pensize(10)

turtle.left(90)
turtle.forward(56)
turtle.right(90)
for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
    turtle.right(10)
    turtle.forward(5)
turtle.penup()
turtle.left(170)
turtle.forward(45)
turtle.left(90)
turtle.pendown()
turtle.forward(56)
turtle.right(90)
for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
    turtle.right(10)
    turtle.forward(3)
turtle.left(125)
turtle.forward(30)

turtle.exitonclick()
