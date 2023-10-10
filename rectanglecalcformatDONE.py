# CST 173 - Delta College
# This program prompts for a rectangle length & width.  It then
# calculates and displays the rectangle area and perimeter

import math

def calcArea(length,width):
    return length * width
    
def calcPerimeter(length,width):
    return 2 * length + 2 * width

def calcDiagonal(length,width):
    return math.sqrt(length * length + width * width)


# Input rectangle attributes
print("For given rectangle:")
length = float(input("==> Enter length (meters): "))
width  = float(input("==> Enter width  (meters): "))

# Processing
area      = calcArea(length,width)
perimeter = calcPerimeter(length,width)
diagonal  = calcDiagonal(length,width)

# Output
print()
print ("For rectangle dimensions",length,"meters X",width,"meters:")
print ("  Perimeter: %8.1f meters"        % (perimeter))
print ("  Area:      %8.2f square meters" % (area))
print ("  Diagonal:  %8.3f square meters" % (diagonal))
