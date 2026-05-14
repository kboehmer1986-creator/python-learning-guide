# This file demonstrates the use of variables in Python.

# Basic variable assignment
name = "Kay Böhmer"
age = 39
is_student = False

# Multiple assignment
city, country, continent = "Erfurt", "Germany", "Europe"

# Constants (by convention, use uppercase)
PI = 3.14159
MAX_CONNECTIONS = 100

# Different data types
integer_var = 42
float_var = 3.14
string_var = "Hello, World!"
boolean_var = True

# Type conversion
num_str = "123"
num_int = int(num_str)  # Convert string to integer
num_float = float(num_str)  # Convert string to float

# Print variables
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Location: {city}, {country}, {continent}")
print(f"PI: {PI}")
print(f"Max Connections: {MAX_CONNECTIONS}")

# Print types
print(f"Type of integer_var: {type(integer_var)}")
print(f"Type of float_var: {type(float_var)}")
print(f"Type of string_var: {type(string_var)}")
print(f"Type of boolean_var: {type(boolean_var)}")

# Print converted values
print(f"num_str: {num_str} (Type: {type(num_str)})")
print(f"num_int: {num_int} (Type: {type(num_int)})")
print(f"num_float: {num_float} (Type: {type(num_float)})")

# Mathematical operations with variables
x = 10
y = 5
sum_result = x + y
difference = x - y
product = x * y
quotient = x / y
modulus = x % y
exponent = x ** y

print(f"\nMathematical Operations:")
print(f"{x} + {y} = {sum_result}")
print(f"{x} - {y} = {difference}")
print(f"{x} * {y} = {product}")
print(f"{x} / {y} = {quotient}")
print(f"{x} % {y} = {modulus}")
print(f"{x} ** {y} = {exponent}")

# String operations
first_name = "Kay"
last_name = "Böhmer"
full_name = first_name + " " + last_name
greeting = f"Hello, {full_name}!"

print(f"\nString Operations:")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Full Name: {full_name}")
print(f"Greeting: {greeting}")

# User input
user_name = input("\nEnter your name: ")
user_age = int(input("Enter your age: "))
print(f"\nUser Input:")
print(f"Hello, {user_name}! You are {user_age} years old.")

# Variable reassignment
print("\nVariable Reassignment:")
counter = 0
print(f"Initial counter value: {counter}")
counter += 1
print(f"Counter after increment: {counter}")
counter *= 2
print(f"Counter after multiplication: {counter}")

# Deleting variables
print("\nDeleting Variables:")
temp_var = 100
print(f"temp_var before deletion: {temp_var}")
del temp_var
# print(temp_var)  # This would raise a NameError since temp_var is deleted

# Checking variable existence
print("\nChecking Variable Existence:")
if 'name' in locals():
    print("Variable 'name' exists.")
else:
    print("Variable 'name' does not exist.")

if 'temp_var' in locals():
    print("Variable 'temp_var' exists.")
else:
    print("Variable 'temp_var' does not exist.")