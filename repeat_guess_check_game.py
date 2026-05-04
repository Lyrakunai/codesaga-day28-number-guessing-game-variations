import random
secret = random.randint(1,10)
guesses = []
for i in range(1,4):
    guess = int(input("guess number between 1 and 10: "))
    if guess in guesses:
        print("you already guessed this number")
        continue
    guesses.append(guess)
    if guess == secret:
        print("congratulations! you guessed it.")
        break
    elif guess > secret:
        print("too high") 
    else:
        print("too low")    
    if i == 3:
        print("game over! The number was", secret)
    
    