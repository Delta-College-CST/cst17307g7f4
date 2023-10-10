# This program evaluates the results of a quiz

def inputScore():
    score = int(input("Enter quiz score: "))
    while(score < 0 or score > 10):
        print("Invalid quiz score - please re-enter")
        score = int(input("Enter quiz score: "))
    return score

# Call function for input and validation
score = inputScore()

# Provide student feedback for the score
if score >= 9:
    print("Excellent work!")
elif score >= 7:
    print("Average score")
elif score >= 5:
    print("Just passing - room for improvement")
else:
    print("Failing grade - let's talk")
