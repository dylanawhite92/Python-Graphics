## TurtleDrawMax.py allows the user to draw turtle graphics
## with the click of their mouse, but gives a bigger pen.
import turtle

t = turtle.Pen()
t.speed(0)

turtle.onscreenclick(t.setpos)

turtle.bgcolor("blue")
t.pencolor("green")

t.width(99)