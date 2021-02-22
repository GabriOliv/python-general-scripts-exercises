#!/usr/bin/env python3.8

# 08
# Make a two-player Rock-Paper-Scissors game.
#   (Hint: Ask for player plays (using input),
#   compare them, print out a message of congratulations to the winner,
#   and ask if the players want to start a new game)

import getpass
import time

speed = 0.2

#Head Output
time.sleep(speed)

print("\n\n\t\tGAME Rock Paper Scissors")

time.sleep(speed)

while True:
    #Head Output
    print("\n\n-------------------------------")

    time.sleep(speed)
    print("  1 [ Rock ]")

    time.sleep(speed)
    print("  2 [ Paper ]")

    time.sleep(speed)
    print("  3 [ Scissors ]")

    time.sleep(speed)
    print("\n  Or Press other number to Exit")

    time.sleep(speed)
    print("-------------------------------\n\n")

    time.sleep(speed)

    #Input
    while True:
        try:
            choose_1 = int(getpass.getpass(" [Player 1]\r"))
            assert (choose_1 == 1 or choose_1 == 2 or choose_1 == 3)
        except ValueError:
            exit()
        except AssertionError:
            exit()
        else:
            break

    while True:
        try:
            choose_2 = int(getpass.getpass(" [Player 2]\r"))
            assert (choose_2 == 1 or choose_2 == 2 or choose_2 == 3)
        except ValueError:
            exit()
        except AssertionError:
            exit()
        else:
            break

    time.sleep(speed)

    #Win Output
    print("\n\n")

    time.sleep(speed)

    print("============================================")

    time.sleep(speed)

    if choose_1 == 1:
        if choose_2 == 1:
            print("  [P1]Rock\t[P2]Rock\tDraw")
        elif choose_2 == 2:
            print("  [P1]Rock\t[P2]Paper\tPlayer 2 WIN")
        elif choose_2 == 3:
            print("  [P1]Rock\t[P2]Scissors\tPlayer 1 WIN")

    elif choose_1 == 2:
        if choose_2 == 1:
            print("  [P1]Paper\t[P2]Rock\tPlayer 1 WIN")
        elif choose_2 == 2:
            print("  [P1]Paper\t[P2]Paper\tDraw")
        elif choose_2 == 3:
            print("  [P1]Paper\t[P2]Scissors\tPlayer 2 WIN")

    elif choose_1 == 3:
        if choose_2 == 1:
            print("  [P1]Scissors\t[P2]Rock\tPlayer 2 WIN")
        elif choose_2 == 2:
            print("  [P1]Scissors\t[P2]Paper\tPlayer 1 WIN")
        elif choose_2 == 3:
            print("  [P1]Scissors\t[P2]Scissors\tDraw")

    time.sleep(speed)

    print("============================================")

    time.sleep(speed+2)
    print("\n")
