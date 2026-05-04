import random
secret = random.randint(1, 20)
for i in range(1, 6):
    guess = int(input("Guess number between 1 and 20: "))
    if guess == secret:
        print("You win")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")
    if i == 5:
        print("Game Over! The number was", secret)