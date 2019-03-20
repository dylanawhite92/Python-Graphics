## TurtleDraw.py allows the user to draw turtle graphics
## with the click of their mouse.
import turtle

t = turtle.Pen()

t.speed(0)

turtle.onscreenclick(t.setpos)