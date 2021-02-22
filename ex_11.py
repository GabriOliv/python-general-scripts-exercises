#!/usr/bin/env python3.8

# 11
# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
#   You can (and should!) use your answer to Exercise 4 to help you.
#   Take this opportunity to practice using functions, described below.


def input_valor():
    while True:
        try:
            numerator = int(input("Enter a Number: "))
            assert numerator >= 2
        except ValueError:
            print("\n[!] Sorry, Only Interger Number ")
        except AssertionError:
            print("\n[!] Sorry, Only Number >= 2")
        else:
            break
    return numerator


def is_prime(number):
    for i in range(2, number):
        if number % i == 0: return False
    return True


if is_prime(input_valor()) == True:
    print("Is Prime")
else:
    print("Is not Prime")

