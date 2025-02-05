import turtle as t
import colorsys as cs

t.setup(700, 700, )
t.speed(0)
t.tracer(10)
t.width(1)
t.bgcolor("black")

for i in range(25):
    for j in range(15):
        # t.color(cs.hls_to_rgb(j/15, i/25, 1))
        t.color(cs.hsv_to_rgb(j / 15, i / 25, 1))
        t.right(90)
        t.circle(160 - i * 3, 90)
        t.left(90)
        t.circle(160 - i * 3, 90)
        t.right(180)
        t.circle(35, 24)
t.hideturtle()

t.done()
