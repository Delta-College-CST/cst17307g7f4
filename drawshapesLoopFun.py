# This program draws multiple triangles.

import turtle
import random

# Create a turtle object
pen = turtle.Turtle()

def drawTriangle(x,y):
    # Reset pen position for new shape
    pen.penup()
    pen.goto(x,y)

    # Draw triangle
    pen.pendown()
    pen.forward(80)
    pen.left(120)
    pen.forward(80)
    pen.left(120)
    pen.forward(80)
    pen.left(120)

def drawSquare(x,y):
    # Reset pen position for new shape
    pen.penup()
    pen.goto(x,y)

    # Draw triangle
    pen.pendown()
    pen.forward(80)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
    
# Set initial position for shape and ready pen
xPos      = -300
yPos      = 200

# Loop to draw 5 triangles.  Shift right and redraw.
# using general coordinates for each.
for x in range(5):
    drawTriangle(xPos,yPos)   # Draw triangle
    xPos = xPos + 100         # Shift pen position to right
 
# Set initial position for shape and ready pen
xPos      = -300
yPos      = -100

# Loop to draw 5 squares.  Shift right and redraw.
# using general coordinates for each.
for x in range(5):
    drawSquare(xPos,yPos)     # Draw square
    xPos = xPos + 100         # Shift pen position to right



