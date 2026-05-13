# This file demonstrates the use of loops in Python.

# --- For Loops ---

# Basic for loop

print("Basic for loop:")
for i in range(5):
    print(f"Current number: {i}")

# For loop with a list

print("\nFor loop with a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# For loop with index and value ( using enumerate )

print("\nFor loop with index and value:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# For loop with a string

print("\nFor loop with a string:")
for char in "Python":
    print(f"Character: {char}")

# For loop with a dictionary

print("\nFor loop with a dictionary:")
person = {"name": "Kay", "age": 39, "city": "Erfurt"}
for key, value in person.items():
    print(f"{key}: {value}")

# For loop with range ( start, stop, step )

print("\nFor loop with range (start, stop, step):")
for i in range(2, 10, 2):
    print(f"Even number: {i}")

# Nested for loops

print("\nNested for loops:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# --- While Loops ---

# Basic while loop

print("\nBasic while loop:")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with user input

print("\nWhile loop with user input:")
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter a command (type 'quit' to exit): ")
    print(f"You entered: {user_input}")

# While loop with a condition

print("\nWhile loop with a condition:")
number = 10
while number > 0:
    print(f"Countdown: {number}")
    number -= 1

# Infinite loop with break

print("\nInfinite loop with break:")
while True:
    user_command = input("Enter 'break' to exit: ")
    if user_command == "break":
        break
    print(f"You entered: {user_command}")

# While loop with else

print("\nWhile loop with else:")
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1
else:
    print("Loop completed successfully!")

# --- Loop Control Statements ---

# Break statement

print("\nBreak statement:")
for i in range(10):
    if i == 5:
        break
    print(f"Number: {i}")

# Continue statement

print("\nContinue statement:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")

# Pass statement

print("\nPass statement:")
for i in range(3):
    if i == 1:
        pass  # Do nothing
    print(f"Number: {i}")

# --- Practical Examples ---

# Sum of numbers from 1 to n

print("\nSum of numbers from 1 to n:")
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of numbers from 1 to {n}: {total}")

# Factorial of a number

print("\nFactorial of a number:")
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num}: {factorial}")

# Fibonacci sequence

print("\nFibonacci sequence:")
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

# Prime number check

print("\n\nPrime number check:")
number_to_check = 17
is_prime = True
if number_to_check < 2:
    is_prime = False
else:
    for i in range(2, int(number_to_check ** 0.5) + 1):
        if number_to_check % i == 0:
            is_prime = False
            break
print(f"{number_to_check} is {'prime' if is_prime else 'not prime'}")

# Multiplication table

print("\nMultiplication table:")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()  # New line after each row