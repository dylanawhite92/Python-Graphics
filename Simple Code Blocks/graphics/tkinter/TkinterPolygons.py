# import tkinter module, set top level widget to tk
# set top level widget of the main window to variable tk
from tkinter import *
tk = Tk()


# define dimensions of canvas widget in pixels
# pack() is a layout/geometry manager built into the tkinter module
# it pads the window with the specified dimensions
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()

# create_polygon() draws out shapes using args that define xy coordinates and angles
canvas.create_polygon(
    10, 10, 100, 10, 100, 110, fill = "", outline = "black"
)

canvas.create_polygon(
    200, 10, 240, 30, 120, 100, 140, 120, fill = "", outline = "black"
)
