# import tkinter module, set top level widget to tk
# import random module for random variables
# set top level widget of the main window to variable tk
from tkinter import *
import random
tk = Tk()

# define dimensions of canvas widget in pixels
# pack() is a layout/geometry manager built into the tkinter module
# it pads the window with the specified dimensions
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()

# list of colors
colors = [
    "green", "blue", "red", "yellow", "orange", 
    "pink", "purple", "magenta", "cyan"
    ]

# define function to sculpt randomly sized/placed rectangles using random integer values
def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill = fill_color)

# run through the colors list and randomly generate
# colored rectangles up to specified width and height dimensions
# it is possible to run off the canvas
for x in colors:
    random_rectangle(400, 400, x)

# old code
# random_rectangle(400, 400, "green")
# random_rectangle(400, 400, "blue")
# random_rectangle(400, 400, "red")
# random_rectangle(400, 400, "yellow")
# random_rectangle(400, 400, "orange")
# random_rectangle(400, 400, "pink")
# random_rectangle(400, 400, "purple")
# random_rectangle(400, 400, "magenta")
# random_rectangle(400, 400, "cyan")
