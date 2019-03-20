# Color Spiral takes the previous Circle and Square Spiral files,
# and adds sides to them to build on the geometric shapes.
import turtle

t = turtle.Pen()
turtle.bgcolor("black")
# You can choose between 2 and 6 sides for some cool shapes.
sides = 6
colors = [
    "red", "yellow", "blue", "orange", "green", 
    "purple", "white", "lemon chiffon", "brown"
]

# In each iteration, the color is determined by comparing the step in the loop against the 
# modulo of the length of the array, and then using that remainder to call the index of the colors array
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
    t.left(90)
