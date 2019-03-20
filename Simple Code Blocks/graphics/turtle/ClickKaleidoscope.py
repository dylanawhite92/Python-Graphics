import random
import turtle

t = turtle.Pen()

t.speed(0)
t.hideturtle()
turtle.bgcolor("black")

# List of colors available 
colors = [
        "red", "yellow", "blue", "green", 
        "orange", "purple", "white", "gray"
]

# Define function for determining random size and color of spirals
def draw_kaleido(x,y):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)

    draw_spiral(x,y, size)
    draw_spiral(-x,y, size)
    draw_spiral(-x,-y, size)
    draw_spiral(x, -y, size)

# Define function for drawing individual spirals
def draw_spiral(x,y, size):
    t.penup()
    t.setpos(x,y)
    t.pendown()

    for m in range(size):
        t.forward(m*2)
        t.left(92)

turtle.onscreenclick(draw_kaleido)