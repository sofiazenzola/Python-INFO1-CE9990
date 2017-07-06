"""
tkflag.py
Draw the Swiss flag in color on a tkinter Canvas widget.
"""
import tkinter              


height = 300 
width = int(height * 3/2) #Wikipedia says aspect ratio of flag is 2:3

#The root widget is the window that will contain everything we draw.
root = tkinter.Tk()
root.title("Swiss Flag")
root.geometry(str(width) + "x" + str(height))

#highlightthickness = 0 allows the canvas to occupy the entire root.
canvas = tkinter.Canvas(root, highlightthickness = 0)
canvas = tkinter.Canvas(root, highlightthickness = 0, background = "red")

"""
Wikipedia says e ratio of the size of the cross to the height is 5:8,
and to the length is 5:12
thickness of the cross is 1/6
"""
crosswidth= 5/12*width
crossthick= 1/6
crossheight = 5/8*height
white = "#FFFFFF"

##vertical rectangle
##canvas.create_rectangle((.5*width)-(crossthick*crosswidth), (.5*height)-(.5*crossheight), (.5*width)+(crossthick*crosswidth), (.5*height)+(.5*crossheight), width = 0, fill = "white")

##horizantal rectangle
##canvas.create_rectangle((.5*width)-(.5*crosswidth),(.5*height-(crossthick*crossheight),(.5*width)+(.5*crosswidth),(.5*height)+(crossthick*crossheight)), width = 0, fill = "white")


def drawPixel(x, y, color):
    """
    Color the pixel at coordinates (x, y).
    """
    assert isinstance(x, int) and isinstance(y, int) and isinstance(color, str)
    canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = color)


y = 0
while y < height:

    x = 0
    while x < width:

        if x > (.5*width)-(crossthick*crosswidth) and x <(.5*width)+(crossthick*crosswidth) and y>(.5*height)-(.5*crossheight) and y<(.5*height)+(.5*crossheight):
            drawPixel(x, y, white)
        elif x > (.5*width)-(.5*crosswidth) and x < (.5*width)+(.5*crosswidth) and y > (.5*height)-(crossthick*crossheight) and y < (.5*height)+(crossthick*crossheight):
           drawPixel(x, y, white) 
        x += 1
    y += 1

#Make the canvas visible by packing it into the root.
canvas.pack(expand = tkinter.YES, fill = "both")

