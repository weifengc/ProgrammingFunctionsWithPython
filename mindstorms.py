'''
This one is use to learn about classes in python.
'''

import turtle

def draw_squre():
    window=turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    counter = 0
    while counter < 4:
        brad.forward(100)
        brad.right(90)
        counter = counter + 1
    window.exitonclick()

draw_squre()
