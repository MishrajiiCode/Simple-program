# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

a = float(input("Enter the first number: "))
b  =float(input("Enter the second number: "))

total_sum = a+b
print(f"Addition: {total_sum}")
total_sub = a-b
print(f"Subtraction: {total_sub}")
total_mul = a*b
print(f"Multiplication: {total_mul}")
total_div = a/b
print(f"Division: {total_div}")


