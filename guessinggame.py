
import random

print("🎮 Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try a bigger number.")

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print("\n🎉 Congratulations! You guessed it!")
        print("The correct number was:", secret_number)
        print("Total attempts:", attempts)
        break

print("\nThanks for playing!")
