import random
secret = random.randint(1, 30)
while True:
    guess = int(input("Choose number between 1 and 30: "))
    if guess == secret:
        print("You win")
        break
    elif guess >= secret - 2 and guess <= secret + 2:
        print("Very Close!")
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")