# Car.py

# Import the turtle module
import turtle

# Set the turtle pen that draws objects to variable t
t = turtle.Pen()

# The turtle pen moves 

# Draw a rectangular, red car body
t.color(1, 0, 0)
t.begin_fill()

# Each forward() indicates the distance in pixels that it moves, 
# each left() and right() indicates turning by degrees,
# the turtle turns and moves with each function
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)

t.end_fill()

# First wheel
# Change the color to black, and move the turtle without drawing a line until begin_fill()
# t.up() effectively 'lifts the pencil' before calling t.down() to begin drawing again at the new coordinates
t.color(0, 0, 0)

t.up()
t.forward(10)
t.down()

t.begin_fill()

t.circle(10)

t.end_fill()

# Move to second wheel and draw
t.setheading(0)

t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)

t.begin_fill()

t.down()
t.circle(10)

t.end_fill()
