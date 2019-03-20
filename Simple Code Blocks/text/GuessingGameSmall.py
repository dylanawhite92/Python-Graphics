import random

# Generate a random number between 1 and 10
the_number = random.randint(1, 10)
# Store user input guess, converting input to an integer in the process
guess = int(input("Guess a number between 1 and 10: "))

while guess != the_number:
    if guess > the_number:
        print(guess, "was too high. Try again.")
    if guess < the_number:
        print(guess, "was too low. Try again.")
    guess = int(input("Guess again: ")) 
print(guess, "was the number! You win!")
