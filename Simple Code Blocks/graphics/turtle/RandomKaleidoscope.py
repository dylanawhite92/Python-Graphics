# KaleidoscopeChallenge.py - Text combined both challenges into one code,
# as opposed to separating the challenges. So only one file for both challenges.
import random
import turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = [
    "red", "yellow", "blue", "green", 
    "orange", "purple", "white", "gray"
]

for n in range(50):
    # Generate spirals of random sizes/colors at random locations on the screen.
    t.pencolor(random.choice(colors))   # Pick a random color from colors[].
    size = random.randint(10,40)        # Pick a random spiral size from 10 to 40.
    sides = random.randint(3,9)         # Pick a random number of sides in spiral
    thick = random.randint(1,6)         # Pick a random thickness of the lines
    t.width(thick)
    angle = t.heading()

    # Generate a random (x,y) location on the screen.
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0,turtle.window_height()//2)

    # First spiral.
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 2)

    # Second spiral.
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    t.setheading(180-angle)

    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 2)
    
    # Third spiral.
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    t.setheading(angle-180)

    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 2)
    
    # Fourth spiral.
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    t.setheading(360-angle)
    
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 2)
