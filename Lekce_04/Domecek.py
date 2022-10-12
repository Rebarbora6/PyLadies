from turtle import color, forward, left, fillcolor, begin_fill, forward, left, end_fill, exitonclick

size = 100
color = "#FFE66D"

fillcolor(color)
begin_fill()

for _ in range(4):
    forward(size)
    left(90)

end_fill()

exitonclick()