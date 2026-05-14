# This file demonstrates Object-Oriented Programming (OOP) in Python with classes.

# --- Basic Class Definition ---
class Dog:
    """A simple class representing a dog."""

    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Create instances of Dog
dog1 = Dog("Buddy", 5)
dog2 = Dog("Milo", 3)

print("--- Basic Class Example ---")
print(dog1.description())  # Buddy is 5 years old.
print(dog2.description())  # Milo is 3 years old.
print(dog1.speak("Woof Woof"))  # Buddy says Woof Woof
print(dog2.speak("Bark Bark"))  # Milo says Bark Bark
print(f"Species: {dog1.species}")  # Canis familiaris

# --- Inheritance ---
class Bulldog(Dog):
    """A class representing a bulldog, inheriting from Dog."""

    # Override class attribute
    species = "Canis familiaris (Bulldog)"

    # Extend the initializer
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    # Override instance method
    def speak(self, sound="Woof Woof"):
        return f"{self.name} the {self.color} bulldog says {sound}"

print("\n--- Inheritance Example ---")
bulldog = Bulldog("Rex", 4, "white")
print(bulldog.description())  # Rex is 4 years old.
print(bulldog.speak())  # Rex the white bulldog says Woof Woof
print(bulldog.speak("Grrr"))  # Rex the white bulldog says Grrr
print(f"Species: {bulldog.species}")  # Canis familiaris (Bulldog)

# --- Class Methods and Static Methods ---
class Pizza:
    """A class representing a pizza."""

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):
        return f"Pizza with {self.ingredients}"

    @classmethod
    def margherita(cls):
        """Factory method to create a Margherita pizza."""
        return cls(["tomato sauce", "mozzarella", "basil"])

    @classmethod
    def prosciutto(cls):
        """Factory method to create a Prosciutto pizza."""
        return cls(["tomato sauce", "mozzarella", "ham"])

    @staticmethod
    def calculate_area(radius):
        """Static method to calculate the area of a pizza."""
        return 3.14159 * radius ** 2

print("\n--- Class Methods and Static Methods ---")
margherita = Pizza.margherita()
prosciutto = Pizza.prosciutto()
print(margherita)  # Pizza with ['tomato sauce', 'mozzarella', 'basil']
print(prosciutto)  # Pizza with ['tomato sauce', 'mozzarella', 'ham']
print(f"Area of a pizza with radius 12: {Pizza.calculate_area(12):.2f}")

# --- Magic Methods (Dunder Methods) ---
class Vector:
    """A class representing a 2D vector."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        """Add two vectors."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract two vectors."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Multiply vector by a scalar."""
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        """Check if two vectors are equal."""
        return self.x == other.x and self.y == other.y

    def __len__(self):
        """Return the magnitude of the vector."""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

print("\n--- Magic Methods Example ---")
v1 = Vector(2, 4)
v2 = Vector(1, 3)
print(f"v1: {v1}")  # Vector(2, 4)
print(f"v2: {v2}")  # Vector(1, 3)
print(f"v1 + v2: {v1 + v2}")  # Vector(3, 7)
print(f"v1 - v2: {v1 - v2}")  # Vector(1, 1)
print(f"v1 * 3: {v1 * 3}")  # Vector(6, 12)
print(f"v1 == Vector(2, 4): {v1 == Vector(2, 4)}")  # True
print(f"Magnitude of v1: {len(v1)}")  # 4 (sqrt(2^2 + 4^2) ≈ 4.47, cast to int)

# --- Property Decorators ---
class Temperature:
    """A class representing temperature with Celsius and Fahrenheit."""

    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Get the temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set the temperature in Celsius."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Get the temperature in Fahrenheit."""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set the temperature in Fahrenheit."""
        self._celsius = (value - 32) * 5/9

print("\n--- Property Decorators Example ---")
temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")  # 25°C
print(f"Fahrenheit: {temp.fahrenheit}°F")  # 77°F

temp.fahrenheit = 100
print(f"Celsius after setting Fahrenheit to 100: {temp.celsius}°C")  # ~37.78°C

# --- Class Composition ---
class Engine:
    """A class representing a car engine."""

    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started."

class Car:
    """A class representing a car."""

    def __init__(self, make, model, engine_horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(engine_horsepower)  # Composition

    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"

print("\n--- Class Composition Example ---")
car = Car("Toyota", "Corolla", 150)
print(car.start())  # Toyota Corolla: Engine started.

# --- Abstract Base Classes (ABC) ---
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def make_sound(self):
        """Abstract method to make a sound."""
        pass

class Cat(Animal):
    """A class representing a cat."""

    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    """A class representing a cow."""

    def make_sound(self):
        return "Moo!"

print("\n--- Abstract Base Classes Example ---")
cat = Cat()
cow = Cow()
print(f"Cat says: {cat.make_sound()}")  # Meow!
print(f"Cow says: {cow.make_sound()}")  # Moo!

# animal = Animal()  # This would raise TypeError

# --- Multiple Inheritance ---
class Father:
    """Class representing a father."""

    def skills(self):
        print("Programming")

class Mother:
    """Class representing a mother."""

    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    """Class representing a child inheriting from both parents."""

    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

print("\n--- Multiple Inheritance Example ---")
child = Child()
child.skills()
# Output:
# Programming
# Cooking
# Sports

# --- Method Resolution Order (MRO) ---
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")
        super().method()

class C(A):
    def method(self):
        print("C method")
        super().method()

class D(B, C):
    def method(self):
        print("D method")
        super().method()

print("\n--- Method Resolution Order Example ---")
d = D()
d.method()
# Output:
# D method
# B method
# C method
# A method

print(f"MRO for D: {D.__mro__}")

# --- Class Variables vs Instance Variables ---
class Employee:
    """Class representing an employee."""

    # Class variable
    company_name = "Tech Corp"
    employee_count = 0

    def __init__(self, name):
        self.name = name  # Instance variable
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

print("\n--- Class Variables vs Instance Variables ---")
emp1 = Employee("Alice")
emp2 = Employee("Bob")
print(f"{emp1.name} works at {emp1.company_name}")  # Alice works at Tech Corp
print(f"{emp2.name} works at {emp2.company_name}")  # Bob works at Tech Corp
print(f"Total employees: {Employee.get_employee_count()}")  # 2

# Modify class variable
Employee.company_name = "New Tech Corp"
print(f"{emp1.name} now works at {emp1.company_name}")  # Alice now works at New Tech Corp

# --- Private and Protected Members ---
class BankAccount:
    """Class representing a bank account."""

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public
        self._balance = balance  # Protected (convention)
        self.__pin = "1234"  # Private

    def get_balance(self):
        return self._balance

    def __authenticate(self, pin):
        return pin == self.__pin

    def withdraw(self, amount, pin):
        if self.__authenticate(pin):
            if amount <= self._balance:
                self._balance -= amount
                return f"Withdrew {amount}. New balance: {self._balance}"
            else:
                return "Insufficient funds."
        else:
            return "Authentication failed."

print("\n--- Private and Protected Members Example ---")
account = BankAccount("Kay", 1000)
print(f"Account holder: {account.account_holder}")  # Kay
print(f"Balance: {account.get_balance()}")  # 1000
print(account.withdraw(200, "1234"))  # Withdrew 200. New balance: 800
print(account.withdraw(1000, "wrong"))  # Authentication failed.
# print(account.__pin)  # AttributeError: 'BankAccount' object has no attribute '__pin'

# --- Practical Examples ---
class Book:
    """Class representing a book."""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} was not checked out."

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

print("\n--- Practical Example: Book Class ---")
book = Book("Python Crash Course", "Eric Matthes", 544)
print(book)  # 'Python Crash Course' by Eric Matthes, 544 pages
print(book.check_out())  # Python Crash Course has been checked out.
print(book.check_out())  # Python Crash Course is already checked out.
print(book.return_book())  # Python Crash Course has been returned.

class Library:
    """Class representing a library."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.check_out()
        return f"Book '{title}' not found."

    def list_books(self):
        return [str(book) for book in self.books]

print("\n--- Practical Example: Library Class ---")
library = Library()
library.add_book(Book("Python Crash Course", "Eric Matthes", 544))
library.add_book(Book("Clean Code", "Robert Martin", 464))
print(library.list_books())
# ["'Python Crash Course' by Eric Matthes, 544 pages", "'Clean Code' by Robert Martin, 464 pages"]
print(library.check_out_book("Clean Code"))  # Clean Code has been checked out.