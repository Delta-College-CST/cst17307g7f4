# This program generates a random salutation.

def sayMessage():
    import random
    selection = random.randrange(1, 4)
    if selection == 0:
        returnMsg = "Hey"
    elif selection == 1:
        returnMsg = "Yo"    
    elif selection == 2:
        returnMsg = "Wazzup"    
    elif selection == 3:
        returnMsg = "How goes it?"
    return returnMsg

print(sayMessage())

    
