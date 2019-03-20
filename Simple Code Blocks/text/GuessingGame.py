# GuessingGame.py

# Import the random module
import random

# Generate a random integer between 1 and 100
num = random.randint(1, 100)

# Run the program until the break statement
while True:
	print("Guess a number between 1 and 100!")
	print("(Enter an integer and press Enter to continue.)")

	# Store user input as guess variable
	guess = input()

	# Convert guess to integer
	i = int(guess)

	# Validate user input against randomly generated number
	if i == num:
		print("You guessed right!")
		break
	elif i < num:
		print("Try higher!")
	elif i > num:
		print("Try lower!")
