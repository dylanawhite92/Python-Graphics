# HighCard.py - except the addition of scorekeeping for a complete War game.
import random

# Declare variables
suits = ["clubs", "diamonds", "hearts", "spades"]
faces = [
    "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "jack", "queen", "king", "ace"
]
keep_going = True
hands = 0
ties = 0
my_score = 0
your_score = 0

# Game Loop
while keep_going and (hands < 26):
    hands += 1
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print("I have the", my_face, "of", my_suit, "!")
    print("You have the", your_face, "of", your_suit, "!")
    if faces.index(my_face) > faces.index(your_face):
        print("I win!")
        my_score += 1 + ties
        ties = 0
    elif faces.index(my_face) < faces.index(your_face):
        print("You win!")
        your_score += 1 + ties
        ties = 0
    else:
        print("It's a tie!")
        ties += 1
    print("Score: Computer", my_score, ", You", your_score)
    answer = input("Hit [Enter] to keep going, or any key to exit: ")
    keep_going = (answer == "")
print("Game Over")
if my_score > your_score:
    print("I win the game!")
elif your_score > my_score:
    print("You win the game!")
else:
    print("It was a tie game!")
