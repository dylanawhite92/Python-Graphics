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

# define function to sculpt randomly sized/placed rectangle using random integer values
def random_rectangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2)

# loop from 0 to 100, therefore running 101 times
# on each iteration, randomly generate an unfilled rectangle on the canvas
for x in range(0, 100):
    random_rectangle(400, 400)
