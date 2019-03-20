import turtle       # Set up turtle graphics
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange",
          "purple", "white", "brown", "gray", "pink" ]
family = []         # Set up an empty list for family names
# Ask for the first name
name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end: ")
# Keep asking for names
while name != "":
    # Add their name to the family list
    family.append(name)
    # Ask for another name, or end
    name = turtle.textinput("My family",
                            "Enter a name, or just hit [ENTER] to end: ")

# Draw a spiral of the names on the screen
for m in range(100):
    t.forward(m*4)
    position = t.position() # Remember this corner of the spiral
    heading = t.heading()   # Remember the direction we were heading
    # Our 'inner' spiral loop draws a rosette
    for n in range(len(family)):
        t.pendown()
        t.pencolor(colors[n%len(family)%10])
        t.write(family[n%len(family)], font = ("Arial", int((m + 4) / 4), "bold"))
        t.right(360/len(family) - 2)
        t.width(m/20)
        t.penup()
        t.forward(m)
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/len(family) + 2)
