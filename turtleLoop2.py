"""
Döngü mekanikleri anlamak için yapılmıştır. Bir amacı yoktur.

I just wanted understand to the loop mechanics with turtle,
unnecessary again,

used turtle.
"""
import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
turtle.speed(0)
col=("red")
turtle.pensize(0)
turtle.pencolor(col)

turtle.pendown()

for i in range(190):
    turtle.forward(i*3)
    turtle.right(225)

turtle.done()