# Practice with various functions


######################################################

# This function receives three integer values.  It will
# print the sum (addition) and the product (multiplication)
# of the numbers

def showNumberInfo(num1, num2, num3):
    print ("Sum:     ",num1 + num2 + num3)
    print ("Product: ",num1 * num2 * num3)

######################################################

# This function receives a name, adds it to a return
# address for Delta College, and prints it.
#   { name }
#   1961 Delta Road
#   University Center, MI  48710

def returnAddress(name):
    print(name)
    print("1961 Delta Road")
    print("University Center, MI  48710")

######################################################

# This function speed from parameters distance and time

def calcSpeed(distance,time ):
    speed = distance / time
    return speed

######################################################
# Main Program
######################################################

# 1 #
showNumberInfo(2,3,4)
print()
showNumberInfo(55,66,77)
print()

# 2 #
returnAddress("Jon Snow")
print()
returnAddress("Daenerys Targaryen")
print()

# 3 #
distance = 220
time  = 3
speed = calcSpeed(distance,time)
print(speed)





