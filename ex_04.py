#!/usr/bin/env python3.8

# 04
# Create a program that asks the user for a number 
# and then prints out a list of all the divisors of that number. 
#   (If you don’t know what a divisor is, 
#   it is a number that divides evenly into another number.
#    For example,13 is a divisor of 26 because 26 / 13 has no remainder.)

while True:
    try:
        numerator = int(input("Enter a Number: "))
        assert numerator > 0
    except ValueError:
        print("\n[!] Sorry, Only Positive Numbers")
    except AssertionError:
        print("\n[!] Sorry, Only Positive Numbers")
    else:
        break

print("\nDivisors of", numerator, "\b:\n")
for i in range(1, (numerator + 1) ):
    if numerator % i == 0:
        print("[", i, "]\t", end="")

print("\n")
