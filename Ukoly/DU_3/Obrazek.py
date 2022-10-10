from cmath import pi
import math
from turtle import forward, right, left, penup, pendown
from turtle import setposition, speed, home, exitonclick, shape
from turtle import title, setup, pencolor, pen, pensize, fillcolor
shape('turtle')
title("Vítejte v obousranném lese")
setup(width=1920, height=1200, startx=0, starty=0)
pen(pencolor="green", pensize=3, fillcolor="red")
speed(55)

amount_of_trees = (1920-40) // 150
amount_of_lines = (1200-40) // 180
beta = (math.atan(3 / 4) * (180 / math.pi))
alpha = 180 - (math.atan(4 / 3) * (180 / math.pi))

penup()
setposition(-940, 580)
pendown()

for c in range(amount_of_lines):
    forward(150 * amount_of_trees)
    right(alpha)
    for b in range(amount_of_trees):
        for a in range(2):
            forward(75)
            left(alpha)
            forward(30)
            right(alpha)
        forward(75)
        right(180 - (2 * beta))
        for a in range(2):
            forward(75)
            right(alpha)
            forward(30)
            left(alpha)
        forward(75)
        left(180 - (2 * beta))
    left(beta)
    forward(180)
    left(90)
forward(150 * amount_of_trees)
left(90)
forward(180*amount_of_lines)

exitonclick()
