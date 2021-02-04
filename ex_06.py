#!/usr/bin/env python3.8

# 06
# Ask the user for a string and print out whether
# this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

text = input("Enter a Text: ")

palindrome = list(text)

palindrome.reverse()

palindrome = ''.join(map(str, palindrome))

size = len(palindrome)

flag = 0

for i in range(size):
    if palindrome[i] != text[i]:
        flag = 1

if flag == 0:
    print("Is a Palindrome")
else:
    print("Is not a Palindrome")
