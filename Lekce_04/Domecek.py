from turtle import color, forward, left, fillcolor, begin_fill, forward, left, end_fill, exitonclick

size = 100
color = "#C676E1"

fillcolor(color)
begin_fill()

for _ in range(6):
    forward(size)
    left(60)

end_fill()

exitonclick()