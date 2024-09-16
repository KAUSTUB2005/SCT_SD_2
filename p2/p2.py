import random

def guess_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Guess the number between 1 and 100!")

    # Loop until the user guesses the correct number
    while guess != random_number:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts.")

# Run the guessing game
guess_number()
