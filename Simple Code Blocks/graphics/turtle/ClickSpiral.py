import random
import turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")

# List of colors available 
colors = [
        "red", "yellow", "blue", "green", 
        "orange", "purple", "white", "gray"
]

# Define function for drawing spirals of random colors and sizes on click
def spiral(x,y):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)

turtle.onscreenclick(spiral)