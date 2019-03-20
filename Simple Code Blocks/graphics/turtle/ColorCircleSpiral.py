# Circle Spiral, but with each side drawn in a different color.
import turtle
t = turtle.Pen()

# List of colors available 
colors = ["red", "yellow", "blue", "green"]
turtle.bgcolor("black")

# In each iteration, the color is determined by comparing the step in the loop against the 
# modulo of the length of the array (4), and then using that remainder to call the index of the colors array
for x in range(100):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.left(91)
