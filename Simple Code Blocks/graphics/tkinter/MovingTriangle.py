# import time module to manipulate time values
import time

# import tkinter module, set top level widget to tk
from tkinter import *
tk = Tk()

# define dimensions of canvas widget in pixels
# pack() is a layout/geometry manager built into the tkinter module
# it pads the window with the specified dimensions
canvas = Canvas(tk, width = 400, height = 200)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)

# loop from 0 to 69, therefore running 70 times
# move() moves the triangle forwards in 5px increments, can be -+ for different speeds
# update() updates/refreshes the canvas, effectively animating the triangle
# time.sleep() delays execution of next iteration by .02 seconds
for x in range(0, 70):
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(0.02)
