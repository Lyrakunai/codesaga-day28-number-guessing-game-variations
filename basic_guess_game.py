import random  
secret = random.randint(1, 20)
attempts = 0
while True:
    guess = int(input("Choose number between 1 and 20: "))
    attempts += 1
    if guess == secret:
        print("You won in", attempts, "attempts")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")
