#!/usr/bin/env python3.10

# 01
# Create a program that
#     Asks the user to enter their name and their age.
#     Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:
#     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
#         (Hint: order of operations exists in Python)
#     Print out that many copies of the previous message on separate lines.
#         (Hint: the string "\n" is the same as pressing the ENTER button)

from datetime import datetime

# Main exercise

def get_name():
	return input("Enter your Name: ")

def get_age():
	while True:
		try:
			age = int(input("Enter your Age: "))
			assert age >= 0
		except ValueError:
			print("\n\tSorry, Only Non-Negative Number.")
		except AssertionError:
			print("\n\tSorry, Only Non-Negative Number.")
		else:
			return age

def calculate_year_to_turn_100(age, now):
	if age <= 100:
		return (100 - age) + now
	else:
		return None

def print_message(name, age, year_to_turn_100):
	print("\n\nName: \t", name, "\nAge: \t", age)
	if year_to_turn_100:
		print("\nYou will get 100 years old in ", year_to_turn_100, "\n")
	else:
		print("\nYou already got 100 years old\n")
	print()

# Extras

def get_message():
	return input("\nTalk a Message: ")

def get_repeat_times():
	while True:
		try:
			repeat_times = int(input("Times to Repeat: "))
			assert repeat_times >= 0
		except ValueError:
			print("\n\tSorry, Only Non-Negative Number.")
		except AssertionError:
			print("\n\tSorry, Only Non-Negative Number.")
		else:
			return repeat_times

def repeat_message(message, repeat_times):
	for x in range(repeat_times):
		print("[ ", (x+1), " ]", "\t", message)

# Main

def main():
	name = get_name()
	age = get_age()
	now = datetime.now().year
	year_to_turn_100 = calculate_year_to_turn_100(age, now)
	print_message(name, age, year_to_turn_100)

	message = get_message()
	repeat_times = get_repeat_times()
	repeat_message(message, repeat_times)

if __name__ == "__main__":
	main()
