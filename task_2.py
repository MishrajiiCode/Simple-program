# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

a = input("Enter your first name: ")
b = input("Enter your last name: ")

total_str= a + " "+ b
print(f"\nHello, {total_str}! Welcome to the Python program.")  