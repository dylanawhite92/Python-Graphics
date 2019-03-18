# import tkinter module
from tkinter import *

# set top level widget of the main window to variable tk
tk = Tk()

# define dimensions of canvas widget in pixels
canvas = Canvas(tk, width = 400, height = 400)

# pack() is a layout/geometry manager built into the tkinter module
# it pads the window with the specified dimensions
canvas.pack()

# path to image
my_image = PhotoImage(file = "C:\\YOUR\\PATH\\TO\\YOUR\\image.png")

# create the chosen image starting at coordinates x1, y1, from the top left corner.    
canvas.create_image(0, 0, anchor = NW, image = my_image)