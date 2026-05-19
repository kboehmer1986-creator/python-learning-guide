# Comprehensive Python Learning Guide: From Beginner to Advanced

- Version: 1.0 ( Free Edition )
- Author: [ Kay Böhmer ]
- Date: May 2026
- License: Creative Commons ( CC0-1.0 license )

## Table of Contents

1. [Introduction to Python](#introduction-to-python)
2. [Python Basics](#python-basics)
3. [Control Flow](#control-flow)
4. [Functions and Modules](#functions--modules)
5. [Data Structures](#data-structures)
6. [File Handling](#file-handling)
7. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
8. [Advanced Python Concepts](#advanced-python-concepts)
9. [Debugging and Testing](#debugging--testing)
10. [Working with Libraries and Frameworks](#working-with-libraries--frameworks)
11. [Practical Exercises and Projects](#practical-exercises--projects)
12. [Quizzes and Knowledge Checks](#quizzes--knowledge-checks)
13. [Interactive Learning Modules](#interactive-learning-modules)
14. [Common Mistakes and Best Practices](#common-mistakes--best-practices)
15. [Free Learning Resources](#free-learning-resources)
16. [FAQs and Troubleshooting](#faqs--troubleshooting)
17. [Appendices](#appendices)

## Introduction to Python

### Why Learn Python

Python is a high-level, interpreted and general-purpose programming language known for its:

- Readability: Clean and easy-to-understand syntax.
- Versatility: Used in web development, data science, AI, automation and more.
- Community Support: Large ecosystem of libraries and frameworks.
- Beginner-Friendliness: Ideal for beginners due to its simplicity.

### Python in Industry & Academia

- Industry: Used by companies like Google, Netflix, NASA and Instagram.
- Academia: Taught in universities worldwide for introductory programming courses.

## Setting Up Python

### Installing Python

- Windows: Download the installer from [python.org](https://www.python.org/downloads/) and run it.
- Linux: Use the package manager ( `sudo apt install python3` ).
- MacOS: Use Homebrew ( `brew install python` ) or download from [python.org](https://www.python.org/downloads/macos/).

### Choosing an IDE

- Beginner-Friendly: Thonny, IDLE or VS Code with Python extension.
- Advanced: PyCharm, Jupyter Notebook or Spyder.

### Using Anaconda ( Optional )

Anaconda is a data science-focused distribution of Python that includes:

- Python interpreter.
- Jupyter Notebook.
- Popular libraries like `NumPy`, `Pandas`, `Matplotlib` and many more.

Download from [anaconda.com](https://www.anaconda.com/products/distribution).

## Python Basics

### Syntax & Indentation

Python uses indentation ( whitespace ) to define code blocks instead of braces `{}`.

#### Example

if 5 > 2:
    print("Five is greater than two!")

### Variables and Data Types

Variables in Python are dynamically typed. Common data types include:

| Type      | Example                      | Description                          |
|-----------|------------------------------|--------------------------------------|
| `int`     | `x = 10`                     | Integer ( whole number )             |
| `float`   | `y = 3.14`                   | Floating-point number                |
| `str`     | `name = "Alice"`             | String ( text )                      |
| `bool`    | `is_valid = True`            | Boolean ( `True` or `False` )        |
| `list`    | `nums = [1, 2, 3]`           | Ordered, mutable collection          |
| `tuple`   | `point = (1, 2)`             | Ordered, immutable collection        |
| `dict`    | `person = {"name": "Alice"}` | Key-value pairs                      |
| `set`     | `unique_nums = {1, 2, 3}`    | Unordered, unique elements           |

#### Example

- age = 39  # int
- price = 19.99  # float
- name = "Kay"  # str
- is_student = True  # bool
- fruits = ["apple", "banana"]  # list
- coordinates = (10, 20)  # tuple
- person = {"name": "Kay", "age": 39}  # dict
- unique_numbers = {1, 2, 3}  # set

### Basic Operators

| Operator | Example       | Description                     |
|----------|---------------|---------------------------------|
| `+`      | `x + y`       | Addition                        |
| `-`      | `x - y`       | Subtraction                     |
| `*`      | `x * y`       | Multiplication                  |
| `/`      | `x / y`       | Division ( returns float )      |
| `%`      | `x % y`       | Modulus ( remainder )           |
| `**`     | `x ** y`      | Exponentiation                  |
| `//`     | `x // y`      | Floor division                  |
| `==`     | `x == y`      | Equal to                        |
| `!=`     | `x != y`      | Not equal to                    |
| `>`      | `x > y`       | Greater than                    |
| `<`      | `x < y`       | Less than                       |
| `and`    | `x and y`     | Logical AND                     |
| `or`     | `x or y`      | Logical OR                      |
| `not`    | `not x`       | Logical NOT                     |

### Input and Output

- `print()`: Outputs text to the console.
- `input()`: Takes user input from the console.

#### Example

name = input("Enter your name: ")
print(f"Hello, {name}!")

### Exercise: Variables and User Input

- Create variables for your name, age and favorite color.
- Print them in a single line using an f-string.
- Ask the user for their name and age, then print a greeting message.

### Solution

### Create variables
 
name = "Kay"
age = 39
favorite_color = "blue"

### Print using f-string
 
print(f"Name: {name}, Age: {age}, Favorite Color: {favorite_color}")

### User input

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print(f"Hello, {user_name}! You are {user_age} years old.")

## Control Flow

### Conditional Statements ( `if`, `elif` and `else` )

### Syntax

- if condition1
    #### Code to execute if condition1 is True.
- elif condition2
    #### Code to execute if condition2 is True.
- else
    #### Code to execute if all conditions are False.

#### Example

age = 18
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

### Loops ( `for` and `while` )

### `for` Loop

for item in sequence:
    #### Code to execute for each item

#### Example

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

### `while` Loop

while condition:
    #### Code to execute while condition is True

#### Example

count = 0
while count < 5:
    print(count)
    count += 1

### Loop Control Statements

- `break`: Exit the loop immediately.
- `continue`: Skip the current iteration.
- `pass`: Do nothing ( placeholder ).

#### Example

### Print odd numbers only

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

### Exit loop when i == 5

for i in range(10):
    if i == 5:
        break
    print(i)

### Exercise: Control Flow

- Write a program that checks if a number is positive, negative or zero.
- Write a `for` loop to print the first 10 even numbers.
- Write a `while` loop to print numbers from 10 to 1.

### Solution

### Check number

num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

### First 10 even numbers

for i in range(2, 21, 2):
    print(i)

### Countdown from 10 to 1

i = 10
while i >= 1:
    print(i)
    i -= 1

## Functions and Modules

### Defining and Calling Functions

### Syntax

def function_name(parameters):
                  #### Code to execute
    return value  # Optional

#### Example

def greet(name):
    return f"Hello, {name}!"

print(greet("Kay"))  # Output: Hello, Kay!

### Parameters and Return Values

- Parameters: Inputs for the function.
- Return: Output of the function ( optional ).

#### Example

def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

### Lambda Functions

### Syntax

lambda arguments: expression

#### Example

square = lambda x: x ** 2
print(square(5))  # Output: 25

### Scope and Lifetime of Variables

- Local Scope: Variables defined inside a function ( only accessible within the function ).
- Global Scope: Variables defined outside functions ( accessible everywhere ).

#### Example

x = 10  # Global variable

def my_func():
    y = 5  # Local variable
    print(x)  # Access global variable

my_func()
print(y)  # Error: y is not defined outside the function

### Importing Modules

- `import module`: Import the entire module.
- `from module import function`: Import a specific function.
- `import module as alias`: Import with an alias.

#### Example

import math
print(math.sqrt(16))  # Output: 4.0

from math import pi
print(pi)  # Output: 3.141592653589793

import numpy as np
print(np.array([1, 2, 3]))

### Exercise: Functions and Modules

- Write a function `is_even(num)` that returns `True` if the number is even, otherwise `False`.
- Write a function `calculate_area(radius)` that calculates the area of a circle ( use `math.pi` ).
- Import the `random` module and write a function `roll_dice()` that returns a random number between 1 and 6.

### Solution

### Check if even

def is_even(num):
    return num % 2 == 0

print(is_even(4))  # Output: True

### Calculate area

import math
def calculate_area(radius):
    return math.pi * radius ** 2

print(calculate_area(5))  # Output: ~78.54

### Roll dice

import random
def roll_dice():
    return random.randint(1, 6)

print(roll_dice())

## Data Structures

### Lists and List Methods

- Lists are ordered, mutable collections.

### Common Methods

| Method          | Description                          | Example                     |
|-----------------|--------------------------------------|-----------------------------|
| `append(x)`     | Add an item to the end               | `fruits.append("orange")`   |
| `extend(iter)`  | Add all items from an iterable       | `fruits.extend(["mango"])`  |
| `insert(i, x)`  | Insert an item at index `i`          | `fruits.insert(1, "kiwi")`  |
| `remove(x)`     | Remove the first occurrence of `x`   | `fruits.remove("banana")`   |
| `pop([i])`      | Remove and return item at index `i`  | `fruits.pop(1)`             |
| `sort()`        | Sort the list in place               | `nums.sort()`               |

#### Example:

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']

### Tuples and Immutability

- Tuples are ordered, immutable collections.

#### Example

point = (10, 20)
x, y = point  # Unpacking
print(x)  # Output: 10

### Dictionaries and Key-Value Pairs

- Dictionaries store key-value pairs.

#### Common Methods

| Method          | Description                          | Example                     |
|-----------------|--------------------------------------|-----------------------------|
| `keys()`        | Return all keys                      | `person.keys()`             |
| `values()`      | Return all values                    | `person.values()`           |
| `items()`       | Return all key-value pairs           | `person.items()`            |
| `get(key)`      | Return value for `key` ( safe )      | `person.get("name")`        |
| `pop(key)`      | Remove and return value for `key`    | `person.pop("age")`         |

#### Example

person = {"name": "Kay", "age": 39, "city": "Erfurt"}
print(person["name"])  # Output: Kay
person["age"] = 39  # Update value
person["job"] = "Developer"  # Add new key-value
print(person)  # Output: {'name': 'Kay', 'age': 39, 'city': 'Erfurt', 'job': 'Developer'}

### Sets and Set Operations

Sets are unordered, unique collections.

### Common Operations

| Operation        | Example               | Description                      |
|------------------|-----------------------|----------------------------------|
| `union()`        | `a.union(b)`          | Union of sets `a` and `b`        |
| `intersection()` | `a.intersection(b)`   | Intersection of sets `a` and `b` |
| `difference()`   | `a.difference(b)`     | Items in `a` but not in `b`      |

#### Example

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # Output: {1, 2, 3, 4, 5}
print(a.intersection(b))  # Output: {3}

### Exercise: Data Structures

- Create a list of the first 10 square numbers.
- Create a dictionary where keys are numbers from 1 to 5 and values are their cubes.
- Create a set of unique words from the string `"hello world hello python"`.

### Solution

### List of squares

squares = [x ** 2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

### Dictionary of cubes

cubes = {x: x ** 3 for x in range(1, 6)}
print(cubes)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

### Set of unique words

text = "hello world hello python"
unique_words = set(text.split())
print(unique_words)  # {'hello', 'world', 'python'}

## File Handling

### Reading/Writing Files

### Syntax

### Writing to a file

with open("filename.txt", "w") as file:
    file.write("Hello, World!")

### Reading from a file

with open("filename.txt", "r") as file:
    content = file.read()
    print(content)

### File Modes

| Mode   | Description                          |
|--------|--------------------------------------|
| `"r"`  | Read ( default )                     |
| `"w"`  | Write ( overwrites existing file )   |
| `"a"`  | Append ( adds to existing file )     |
| `"r+"` | Read and write                       |

#### Example

### Write to a file

with open("example.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3")

### Read from a file

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

### Exercise: File Handling

- Write a program that reads a text file and counts the number of lines.
- Write a program that writes a list of dictionaries to a JSON file.
- Write a program that reads a CSV file and prints the first row.

### Solution

### Count lines in a file

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")

### Write list of dictionaries to JSON

import json
people = [
    {"name": "Kay", "age": 39},
    {"name": "Alice", "age": 30}
]
with open("people.json", "w") as file:
    json.dump(people, file)

### Read first row of CSV

import csv
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    first_row = next(reader)
    print(first_row)

## Object-Oriented Programming ( OOP )

### Classes & Objects

### Syntax

class ClassName:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method_name(self):
        #### Method code
        pass

#### Example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name} and I'm {self.age} years old."

### Create an object

person = Person("Kay", 39)
print(person.greet())

### Exercise: OOP

- Create a `Car` class with attributes `make`, `model` and `year`. Add a method `display_info()` to print the cars details.
- Create a `ElectricCar` class that inherits from `Car` and adds a `battery_size` attribute.
- Override the `display_info()` method in `ElectricCar` to include the battery size.

### Solution

### Car class

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

### ElectricCar class

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} (Battery: {self.battery_size} kWh)")

### Test

car = Car("Toyota", "Corolla", 2020)
car.display_info()  # Output: 2020 Toyota Corolla

electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
electric_car.display_info()  # Output: 2022 Tesla Model S ( Battery: 100 kWh )

## Advanced Python Concepts

### Decorators

- Decorators modify the behavior of functions.

### Syntax

def decorator(func):
    def wrapper(*args, **kwargs):
        #### Code before function
        result = func(*args, **kwargs)
        #### Code after function
        return result
    return wrapper

@decorator
def my_function():
    pass

#### Example

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(3, 5))

### Exercise: Advanced Python

- Write a decorator `timer` that measures the execution time of a function.
- Write a generator function `fibonacci(n)` that yields the first `n` Fibonacci numbers.

### Solution

### Timer decorator

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()

### Fibonacci generator

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

## Debugging & Testing

### Debugging with `pdb`

- Python Debugger ( `pdb` ) allows stepping through code.

#### Example

import pdb

def divide(a, b):
    pdb.set_trace()  # Start debugger
    return a / b

divide(10, 2)

### Commands

- `n` ( next line )
- `c` ( continue )
- `q` ( quit )
- `p <variable>` ( print variable )

### Exercise: Debugging and Testing

- Write a unit test for a function `multiply(a, b)` that returns `a * b`.

### Solution

import unittest

def multiply(a, b):
    return a * b

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)

if __name__ == "__main__":
    unittest.main()

## Working with Libraries and Frameworks

### Virtual Environments

### Create a virtual environment

`python -m venv myenv`       # Create

### Activate a virtual environment

`source myenv/bin/activate`  # Linux / Mac
`myenv\Scripts\activate`     # Windows

### Deactivate a virtual environment

`deactivate`                # Deactivate

### Install packages

`pip install package_name`

### Exercise: Libraries and Frameworks

- Install `requests` and write a script to fetch the HTML of a webpage.

### Solution

import requests

response = requests.get("https://www.example.com")
print(response.text[:100])  # Print the first 100 characters.

## Practical Exercises and Projects

### Beginner Projects

- Hello World: Print "Hello, World!" to the console.
- Temperature Converter: Convert between Celsius, Fahrenheit and Kelvin.

#### Example: Temperature Converter

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

if unit == "C":
    print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
elif unit == "F":
    print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")

## Quizzes and Knowledge Checks

### Python Basics Quiz

### What is the output of `print(10 % 3)`?

- A) 1
- B) 2
- C) 3
- D) 0

#### Answer

- A) 1

### Which of the following is not a valid variable name in Python?
 
- A) `_name`
- B) `1name`
- C) `name1`
- D) `name_1`

#### Answer

- B) `1name`

## Interactive Learning Modules

### Jupyter Notebooks

### Install JupyterLab

`pip install jupyterlab`

### Start JupyterLab

`jupyter lab`

### Create a Notebook

- Mix Markdown for explanations and code cells for Python code.

#### Example

### Code cell

def greet(name):
    return f"Hello, {name}!"

greet("Kay")

### Output

'Hello, Kay!'

## Common Mistakes and Best Practices

### Common Mistakes

| Mistake                       | Example                          | Fix                                     |
|-------------------------------|----------------------------------|-----------------------------------------|
| Indentation Errors            | `if x > 0:\nprint("Positive")`   | Use consistent indentation ( 4 spaces ).|
| Missing Colon                 | `if x > 0` (no `:`)              | Add `:` after `if`, `for`, `while`.     |
| Using `=` instead of `==`     | `if x = 5:`                      | Use `==` for comparison.                |

### Follow PEP 8 Guidelines

- Use 4 spaces for indentation.
- Limit lines to 79 characters.
- Use snake_case for variables/functions ( `my_variable` ).
- Use PascalCase for classes ( `MyClass` ).

### Write Readable Code

- Use meaningful variable names ( `num_students` instead of `ns` ).
- Add comments to explain complex logic.

## Free Learning Resources

| Resource                     | Description                                      | Link                                                              |
|------------------------------|--------------------------------------------------|-------------------------------------------------------------------|
| Official Python Docs         | Comprehensive tutorials and references.          | [python.org](https://docs.python.org/3/)                          |
| W3Schools Python             | Beginner-friendly examples.                      | [w3schools.com/python](https://www.w3schools.com/python/)         |
| Codecademy ( Free Tier )     | Interactive Python course.                       | [codecademy.com](https://www.codecademy.com/learn/learn-python-3) |
| LearnPython.org              | Free interactive tutorial.                       | [learnpython.org](https://www.learnpython.org/)                   |
| edX ( Harvard’s CS50P )      | Free university-level course.                    | [edx.org/cs50p](https://cs50.harvard.edu/python/2022/)            |
| YouTube Tutorials            | Free video courses ( Corey Schafer ).            | [YouTube](https://www.youtube.com/)                               |

## FAQs & Troubleshooting

### How to Install Python on Windows / Mac / Linux

- Windows: Download from [python.org](https://www.python.org/downloads/) and run the installer.
- Mac: Use Homebrew ( `brew install python` ) or download from [python.org](https://www.python.org/downloads/macos/).
- Linux: Use the package manager ( `sudo apt install python3` ).

### Why am I getting IndentationError

- Cause: Inconsistent indentation ( mixing tabs and spaces or incorrect indentation ).
- Fix: Use 4 spaces for indentation and ensure consistency.

### What’s the difference between `==` and `is`

- `==`: Checks if two objects have the same value.
- `is`: Checks if two objects are the same object in memory.

#### Example

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)  # True ( same value )
print(a is b)  # True ( same object )
print(a == c)  # True ( same value )
print(a is c)  # False ( different objects )

## Appendices

## Appendix A: Python Cheat Sheet

### Basic Syntax

### Variables
x = 10
name = "Kay"

### Lists
lst = [1, 2, 3]
lst.append(4)

### Functions
def add(a, b):
    return a + b

#### Common Functions

| Function          | Description                          | Example                          |
|-------------------|--------------------------------------|----------------------------------|
| `len(x)`          | Length of `x` ( list, string )       | `len([1, 2, 3])` → `3`           |
| `range(n)`        | Generate numbers from 0 to `n-1`     | `list(range(5))` → `[0,1,2,3,4]` |
| `type(x)`         | Type of `x`                          | `type(10)` → `<class 'int'>`     |
| `str(x)`          | Convert `x` to string                | `str(10)` → `"10"`               |

### File Handling

### Read file

with open("file.txt", "r") as file:
    content = file.read()

### Write file

with open("file.txt", "w") as file:
    file.write("Hello, World!")

### OOP Basics

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}!"

person = Person("Kay", 39)
print(person.greet())

## Appendix B: Glossary of Terms

| Term               | Definition                                                                 |
|--------------------|----------------------------------------------------------------------------|
| Algorithm          | A step-by-step procedure for solving a problem.                            |
| API                | Application Programming Interface ( allows software to communicate ).        |
| Class              | A blueprint for creating objects.                                          |
| Function           | A reusable block of code that performs a specific task.                    |
| Module             | A file containing Python code ( functions, classes, ).                  |
| Object             | An instance of a class.                                                    |
| Variable           | A named storage location for data.                                         |

## Appendix C: Recommended Tools

| Tool               | Description                                      | Link                                                        |
|--------------------|--------------------------------------------------|-------------------------------------------------------------|
| VS Code            | Lightweight, customizable code editor.           | [code.visualstudio.com](https://code.visualstudio.com/)     |
| PyCharm            | Full-featured Python IDE.                        | [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/) |
| JupyterLab         | Interactive development environment.             | [jupyter.org](https://jupyter.org/)                         |
| Git                | Version control system.                          | [git-scm.com](https://git-scm.com/)                         |
| GitHub             | Hosting service for Git repositories.            | [github.com](https://github.com/)                           |