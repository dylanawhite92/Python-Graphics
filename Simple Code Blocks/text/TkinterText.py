# import tkinter module, set top level widget to tk
# set top level widget of the main window to variable tk
from tkinter import *
tk = Tk()

# define dimensions of canvas widget in pixels
# pack() is a layout/geometry manager built into the tkinter module
# it pads the window with the specified dimensions
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()

# create text at specified coordinates, and with specified font and size if applicable
canvas.create_text(150, 100, text = "There once was a man from Toulouse,")
canvas.create_text(130, 120, text = "Who rode around on a moose.", fill = "red")
canvas.create_text(
    150, 150, text = 'He said, "It\'s my curse,', font = ("Times", 15)
)
canvas.create_text(
    200, 200, text = "But it could be worse,", font = ("Helvetica", 20)
)
canvas.create_text(
    220, 250, text = "My cousin rides 'round", font = ("Courier", 22)
)
canvas.create_text(220, 300, text = "on a goose.", font = ("Courier", 30))
