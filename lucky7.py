# The program simulates 100 throws of 2 dice.  It counts
# the occurences of "lucky 7"

NUM_THROWS = 100

def throw2dice():
    import random
    die1 = random.randrange(6) + 1
    die2 = random.randrange(6) + 1
    return die1 + die2

# Simulation loop - count to 100 and track 7's
gotta7 = 0
for throws in range(0,NUM_THROWS):
    throw = throw2dice()
    if throw == 7:
        gotta7 = gotta7 + 1

# Write output
print("For",NUM_THROWS,"throws:", gotta7, "were 7\'s")
