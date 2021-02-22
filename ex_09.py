#!/usr/bin/env python3.8

# 09
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
#   Keep the game going until the user types “exit”
#   Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
import time

speed = 0.1

rand_min = 1
rand_max = 9


# Choose List
a = []
for i in range(9):
    a.append(str(i+1))


# Exit List
b = ["e", "exit"]


a.extend(b)
guess = 0
x = random.randint(1,9)


time.sleep(speed)
print("\n Guessing Game One \n")
time.sleep(speed)
print("\n Number: X", "\t[Between", rand_min, "n", rand_max, "\b]", "\n\n")


while guess != x:
    while True:
        try:
            time.sleep(speed)
            print("[Try Guess] >> [", rand_min, "<->", rand_max, "]")
            time.sleep(speed)
            print("[Stop Game] >> [exit or e]")

            choose_input = input("\nInput:")
            assert choose_input in a

        except AssertionError:
            time.sleep(speed)
            print("\n[!] Sorry, Wrong Input\n")
            time.sleep(speed*3)

        else:
            if choose_input in b:
                exit()
            else:
                guess = int(choose_input)
            break


    time.sleep(speed)
    if guess > x:
        print("\n[!] Too High\n")
    elif guess < x:
        print("\n[!] Too Low\n")
    elif guess == x:
        print("\n[!] Exactly Right\n")
        print("\n\t[!] Number is", guess)
        print("\n\n\t[ YOU WIN ]\n\n")

