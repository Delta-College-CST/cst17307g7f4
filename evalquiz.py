# This program evaluates the results of a quiz

score = int(input("Enter quiz score: "))

# Provide student feedback for the score
if score >= 9:
    print("Excellent work!")
elif score >= 7:
    print("Average score")
elif score >= 5:
    print("Just passing - room for improvement")
else:
    print("Failing grade - let's talk")
