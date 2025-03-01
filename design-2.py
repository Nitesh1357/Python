from turtle import *
from colorsys import *
tracer(10)
bgcolor("black")
h = 0.25
pensize(2)
def draw(x, y):
    circle(5+y, 60)
    left(x)
    circle(5+y, 60)
for i in range(137):
    color(hls_to_rgb(1, h, 0))
    h += 0.0055
    fillcolor('black')
    begin_fill()
    draw(90, i/2)
    end_fill()
    draw(160, i*1.2)
    penup()
    draw(180, i/2)
    draw(90, i/2)
    pendown()
done()
