from turtle import *
from colorsys import *
tracer(10)
bgcolor("black")
h = 0
pensize(2)
for i in range(100):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.002
    up()
    fd(i)
    down()
    forward(i)
    circle(i, -300)
    forward(5)
done()
