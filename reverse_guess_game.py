low = 1
high = 50

print("Think of a number between 1 and 50")
while True:
    guess = (low + high) // 2
    print("Is your number", guess, "?")
    feedback = input("Enter high / low / correct: ")
    
    if feedback == "high":
        high = guess - 1
    elif feedback == "low":
        low = guess + 1
    elif feedback == "correct":
        print("Yay! Computer found your number")
        break
    else:
        print("Invalid input")