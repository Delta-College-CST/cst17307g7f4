# This program calculates the cost for a catering event

def calcCateringCost(numVisitors):
    if numVisitors <= 20:
        costPerPerson = 150
    elif numVisitors <= 50:
        costPerPerson = 130
    elif numVisitors <= 100:
        costPerPerson = 110
    else:
        costPerPerson = 100

    # Calculate cost
    cost =  costPerPerson* numVisitors
    return cost

# ------------------------------------------------------ #

# Prompt for input.
headcount = int(input("Enter number people attending: "))
                
# If not valid, provide specific message.
# Otherwise, determine unit cost for given count.
if headcount <= 0:
    print("Invalid input.")
elif headcount > 200:
    print("Count too large.")
else:
    cost = calcCateringCost(headcount)

    # Display output report
    print()
    print("CATERING ORDER")
    print("Serving:",headcount, "| Cost: $%8.2f" % (cost))
