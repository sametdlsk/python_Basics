"""
Döngü mekanikleri anlamak için yapılmıştır. Bir amacı yoktur.

I just wanted understand to the loop mechanics with turtle,
unnecessary againAndAgain :),

used turtle.
"""

import turtle

turtle.bgcolor("dimgray")

turtle.pensize(2)
turtle.speed(0)
turtle.pencolor('turquoise')

def drawcircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius=radius-2

def drawdesign():
    for i in range(20):
        drawcircle(140)
        turtle.right(26)

drawdesign()
turtle.done()
