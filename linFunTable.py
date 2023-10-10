# This program generates a table of (x,y) values for the function y=3x-7

def linFunction(x):
    y = 3 * x - 7
    return y

# Output table
print("Function:  y = 3 * x -7","\n")
print("  x     y")
print(" --    --")
for x in range(1,21):
    y = linFunction(x)
    print("%3d %5d" % (x,y))
