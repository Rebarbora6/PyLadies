from math import pi, atan
from turtle import forward, right, left, penup, pendown,\
setposition, speed, home, exitonclick, shape,\
title, setup, pencolor, pen, pensize, fillcolor, window_height, window_width

window_width = 1920
window_height = 1200
shape('turtle')
title("Vítejte v obousranném lese")
setup(width=window_width, height=window_height, startx=0, starty=0)
pen(pencolor="green", pensize=3, fillcolor="red")
speed(55)

amount_of_trees = (window_width-40) // 150
amount_of_lines = (window_height-40) // 180
beta = (atan(3 / 4) * (180 / pi))
alpha = 180 - (atan(4 / 3) * (180 / pi))

penup()
setposition(-940, 560)
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
