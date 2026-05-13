# This file demonstrates the use of functions in Python.

# --- Basic Functions ---

# Function without parameters

def greet():
    """This function prints a greeting message."""
    print("Hello, World!")

# Function with parameters

def greet_user(name):
    """This function greets the user by name."""
    print(f"Hello, {name}!")

# Function with default parameters

def greet_user_default(name="User"):
    """This function greets the user with a default name."""
    print(f"Hello, {name}!")

# Function with return value

def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b

# Function with multiple return values

def min_max(numbers):
    """This function returns the minimum and maximum of a list."""
    return min(numbers), max(numbers)

# --- Calling Functions ---

print("--- Basic Function Calls ---")
greet()
greet_user("Kay")
greet_user_default()
greet_user_default("Alice")
print(f"Sum: {add(3, 5)}")
minimum, maximum = min_max([4, 2, 9, 7, 5])
print(f"Min: {minimum}, Max: {maximum}")

# --- Function Arguments ---

# Positional arguments

def subtract(a, b):
    """Subtracts b from a."""
    return a - b

print(f"\nSubtraction (positional): {subtract(10, 3)}")

# Keyword arguments

print(f"Subtraction (keyword): {subtract(b=3, a=10)}")

# Arbitrary number of arguments ( *args )

def sum_all(*args):
    """Returns the sum of all arguments."""
    return sum(args)

print(f"Sum of arbitrary args: {sum_all(1, 2, 3, 4)}")

# Arbitrary number of keyword arguments ( **kwargs )

def print_info(**kwargs):
    """Prints all key-value pairs."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\nPrinting info:")
print_info(name="Kay", age=39, city="Erfurt")

# --- Lambda Functions ---

print("\n--- Lambda Functions ---")

# Simple lambda function

square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments

multiply = lambda x, y: x * y
print(f"5 * 3: {multiply(5, 3)}")

# Using lambda with built-in functions

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# --- Scope and Lifetime of Variables ---

# Global variable

global_var = 10

def access_global():
    """Accesses a global variable."""
    print(f"Global variable inside function: {global_var}")

def modify_global():
    """Modifies a global variable."""
    global global_var
    global_var = 20
    print(f"Modified global variable: {global_var}")

print("\n--- Variable Scope ---")
print(f"Global variable outside function: {global_var}")
access_global()
modify_global()
print(f"Global variable after modification: {global_var}")

# Local variable

def local_example():
    """Demonstrates local variable scope."""
    local_var = 5
    print(f"Local variable inside function: {local_var}")

local_example()

# print(local_var)  # This would raise a NameError

# --- Nested Functions ---

print("\n--- Nested Functions ---")

def outer_function(text):
    """Demonstrates nested functions."""
    def inner_function():
        return text.upper()
    return inner_function()

print(outer_function("hello"))

# --- Recursive Functions ---

print("\n--- Recursive Functions ---")

# Factorial

def factorial(n):
    """Calculates the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Fibonacci

def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci(7): {fibonacci(7)}")

# --- Higher-Order Functions ---

print("\n--- Higher-Order Functions ---")

# Function as an argument

def apply_function(func, value):
    """Applies a function to a value."""
    return func(value)

def double(x):
    return x * 2

print(f"Applied double function: {apply_function(double, 5)}")

# Function returning a function

def create_multiplier(factor):
    """Returns a function that multiplies by factor."""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(f"Double of 5: {double(5)}")
print(f"Triple of 5: {triple(5)}")

# --- Decorators ---

print("\n--- Decorators ---")

# Simple decorator

def my_decorator(func):
    """A simple decorator."""
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with arguments

def repeat(num_times):
    """Decorator factory that repeats a function."""
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet_repeat(name):
    print(f"Hello, {name}!")

greet_repeat("Kay")

# --- Docstrings and Function Documentation ---

print("\n--- Docstrings ---")

def example_function(param1, param2):
    """
    This is an example function with a docstring.

    Parameters:
    param1 (int): The first parameter.
    param2 (str): The second parameter.

    Returns:
    str: A message combining param1 and param2.
    """
    return f"{param1} - {param2}"

print(example_function.__doc__)
print(f"Function call: {example_function(42, 'Answer')}")

# --- Built-in Functions ---

print("\n--- Built-in Functions ---")

# Using map

numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers: {doubled}")

# Using filter

even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even}")

# Using reduce

from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of numbers: {product}")

# --- Practical Examples ---

print("\n--- Practical Examples ---")

# Temperature conversion

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

print(f"30°C in Fahrenheit: {celsius_to_fahrenheit(30):.2f}°F")
print(f"86°F in Celsius: {fahrenheit_to_celsius(86):.2f}°C")

# String manipulation

def reverse_string(s):
    """Reverses a string."""
    return s[::-1]

def is_palindrome(s):
    """Checks if a string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == reverse_string(s)

print(f"Reversed 'hello': {reverse_string('hello')}")
print(f"Is 'madam' a palindrome? {is_palindrome('madam')}")

# List operations

def flatten_list(nested_list):
    """Flattens a nested list."""
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

nested = [1, [2, [3, 4], 5], 6]
print(f"Flattened list: {flatten_list(nested)}")