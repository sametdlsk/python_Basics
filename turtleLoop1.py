"""
Döngü mekanikleri anlamak için yapılmıştır. Bir amacı yoktur.

I just wanted understand to the loop mechanics with turtle,
unnecessary,

used turtle.
"""

import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(20):
    for colours in ["dimgray", "dimgrey", "gray", "grey", "darkgray", "darkgrey", "silver", "lightgray", "lightgrey"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()
