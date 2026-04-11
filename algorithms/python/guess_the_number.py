"""
Guess The Number

Simple game: guess a random number between 2 and 100.
You have 5 attempts. Feedback tells you if you're too high or too low.
"""

import random

result = random.randint(2, 100)
counter = [0]

for _ in counter:
    try:
        price = int(input("What number do you want to guess? "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if price == result:
        print("You won! Congratulations!!")
        break

    elif price > result:
        print("Too high! You need to go lower.")
        counter.append(1)
    else:
        print("Too low! You need to go higher.")
        counter.append(1)

    if sum(counter) == 6:
        print("You lost! Better luck next time.")
        print(f"The correct number was {result}")
        break
