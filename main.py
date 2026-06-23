import random

comp=random.randint(1,100)
print("Welcome to the Number Guessing Game!")
try:
    while True:
        user=int(input("Enter a number between 1 and 100: "))
        if user<comp:
            print("Too low! Try again.")
        elif user>comp:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            break
except ValueError:
    print("Invalid input! Please enter a valid number.")