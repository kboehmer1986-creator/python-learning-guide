# This file demonstrates inheritance concepts in Python.

# --- Single Inheritance ---

class Animal:
    """Base class representing an animal."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        """Make a generic animal sound."""
        return "Some generic animal sound"

    def describe(self):
        """Describe the animal."""
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    """Derived class representing a dog, inheriting from Animal."""

    def __init__(self, name, breed):
        # Call the parent class's __init__ method
        super().__init__(name, species="Canis familiaris")
        self.breed = breed

    def make_sound(self):
        """Override the parent's make_sound method."""
        return "Woof! Woof!"

    def fetch(self):
        """Method specific to Dog class."""
        return f"{self.name} is fetching the ball!"

print("--- Single Inheritance Example ---")
animal = Animal("Generic", "Unknown")
print(animal.describe())  # Generic is a Unknown
print(animal.make_sound())  # Some generic animal sound

dog = Dog("Buddy", "Golden Retriever")
print(dog.describe())  # Buddy is a Canis familiaris
print(dog.make_sound())  # Woof! Woof!
print(dog.fetch())  # Buddy is fetching the ball!

# --- Multiple Inheritance ---

class Father:
    """Class representing a father."""

    def __init__(self, name):
        self.father_name = name

    def skills(self):
        """Father's skills."""
        print("Programming")

    def advice(self):
        """Father's advice."""
        return "Work hard and be honest."

class Mother:
    """Class representing a mother."""

    def __init__(self, name):
        self.mother_name = name

    def skills(self):
        """Mother's skills."""
        print("Cooking")

    def advice(self):
        """Mother's advice."""
        return "Be kind to everyone."

class Child(Father, Mother):
    """Class representing a child inheriting from both Father and Mother."""

    def __init__(self, name, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.name = name

    def skills(self):
        """Child's skills - calls both parents' skills."""
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

    def advice(self):
        """Child's advice - combines both parents' advice."""
        father_advice = Father.advice(self)
        mother_advice = Mother.advice(self)
        return f"Father says: '{father_advice}' and Mother says: '{mother_advice}'"

print("\n--- Multiple Inheritance Example ---")
child = Child("Alice", "John", "Jane")
print(f"Child's name: {child.name}")
print(f"Father's name: {child.father_name}")
print(f"Mother's name: {child.mother_name}")
child.skills()

# Output:
# Programming
# Cooking
# Sports

print(child.advice())

# Output: Father says: 'Work hard and be honest.' and Mother says: 'Be kind to everyone.'

# --- Method Resolution Order ( MRO ) ---

class A:
    def method(self):
        print("A method")
        super().method()

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

# Output: ( <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'> )

# --- Hierarchical Inheritance ---

class Vehicle:
    """Base class representing a vehicle."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        """Display vehicle information."""
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    """Derived class representing a car."""

    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def display_info(self):
        """Override display_info to include number of doors."""
        base_info = super().display_info()
        return f"{base_info} with {self.num_doors} doors"

class Motorcycle(Vehicle):
    """Derived class representing a motorcycle."""

    def __init__(self, brand, model, has_sidecar):
        super().__init__(brand, model)
        self.has_sidecar = has_sidecar

    def display_info(self):
        """Override display_info to include sidecar information."""
        base_info = super().display_info()
        sidecar_info = "with sidecar" if self.has_sidecar else "without sidecar"
        return f"{base_info} {sidecar_info}"

print("\n--- Hierarchical Inheritance Example ---")
vehicle = Vehicle("Generic", "Model")
print(vehicle.display_info())  # Generic Model

car = Car("Toyota", "Corolla", 4)
print(car.display_info())  # Toyota Corolla with 4 doors

motorcycle = Motorcycle("Harley-Davidson", "Sportster", False)
print(motorcycle.display_info())  # Harley-Davidson Sportster without sidecar

# --- Multilevel Inheritance ---

class Grandparent:
    """Base class representing a grandparent."""

    def __init__(self, name):
        self.name = name

    def tell_story(self):
        """Grandparent's method."""
        return f"{self.name} tells an old story."

class Parent(Grandparent):
    """Derived class representing a parent."""

    def __init__(self, name, parent_name):
        super().__init__(name)
        self.parent_name = parent_name

    def give_advice(self):
        """Parent's method."""
        return f"{self.parent_name} gives some advice."

class Child(Parent):
    """Derived class representing a child."""

    def __init__(self, name, parent_name, child_name):
        super().__init__(name, parent_name)
        self.child_name = child_name

    def play(self):
        """Child's method."""
        return f"{self.child_name} is playing."

print("\n--- Multilevel Inheritance Example ---")
child = Child("Grandpa", "Dad", "Alice")
print(child.tell_story())  # Grandpa tells an old story.
print(child.give_advice())  # Dad gives some advice.
print(child.play())  # Alice is playing.

# --- Inheritance with Magic Methods ---

class Shape:
    """Base class representing a shape."""

    def __init__(self, color):
        self.color = color

    def area(self):
        """Calculate area of the shape."""
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self):
        return f"A {self.color} shape"

class Circle(Shape):
    """Derived class representing a circle."""

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        """Calculate area of the circle."""
        return 3.14159 * self.radius ** 2

    def __str__(self):
        return f"A {self.color} circle with radius {self.radius}"

class Rectangle(Shape):
    """Derived class representing a rectangle."""

    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of the rectangle."""
        return self.width * self.height

    def __str__(self):
        return f"A {self.color} rectangle with width {self.width} and height {self.height}"

print("\n--- Inheritance with Magic Methods Example ---")
shapes = [Circle("red", 5), Rectangle("blue", 4, 6)]

for shape in shapes:
    print(shape)
    print(f"Area: {shape.area():.2f}")
    print()

# --- Abstract Base Classes (ABC) with Inheritance ---

from abc import ABC, abstractmethod

class Instrument(ABC):
    """Abstract base class representing a musical instrument."""

    @abstractmethod
    def play(self):
        """Abstract method to play the instrument."""
        pass

    @abstractmethod
    def tune(self):
        """Abstract method to tune the instrument."""
        pass

class StringInstrument(Instrument):
    """Abstract class representing a string instrument."""

    def __init__(self, num_strings):
        self.num_strings = num_strings

    def tune(self):
        """Tune the string instrument."""
        return f"Tuning {self.num_strings} strings."

class Guitar(StringInstrument):
    """Concrete class representing a guitar."""

    def play(self):
        """Play the guitar."""
        return "Strumming the guitar."

    def tune(self):
        """Override tune method for Guitar."""
        base_tune = super().tune()
        return f"{base_tune} Standard tuning: EADGBE"

class Violin(StringInstrument):
    """Concrete class representing a violin."""

    def play(self):
        """Play the violin."""
        return "Playing the violin with a bow."

print("\n--- Abstract Base Classes with Inheritance Example ---")
guitar = Guitar(6)
print(guitar.play())  # Strumming the guitar.
print(guitar.tune())  # Tuning 6 strings. Standard tuning: EADGBE

violin = Violin(4)
print(violin.play())  # Playing the violin with a bow.
print(violin.tune())  # Tuning 4 strings.

# --- Inheritance with Class Methods and Static Methods ---

class Product:
    """Base class representing a product."""

    tax_rate = 0.20  # Class attribute

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total_price(self):
        """Calculate total price including tax."""
        return self.price * (1 + self.tax_rate)

    @classmethod
    def set_tax_rate(cls, rate):
        """Class method to set the tax rate."""
        cls.tax_rate = rate

    @staticmethod
    def calculate_discount(price, discount_percent):
        """Static method to calculate discount."""
        return price * (1 - discount_percent / 100)

class ElectronicProduct(Product):
    """Derived class representing an electronic product."""

    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def total_price(self):
        """Override total_price to include warranty cost."""
        base_price = super().total_price()
        return base_price + 20  # Additional warranty cost

print("\n--- Inheritance with Class Methods and Static Methods Example ---")
product = Product("Book", 50)
print(f"Book total price: {product.total_price():.2f}")  # 60.00

# Change tax rate for all products

Product.set_tax_rate(0.25)
print(f"Book total price after tax change: {product.total_price():.2f}")  # 62.50

# Calculate discount

discounted_price = Product.calculate_discount(100, 10)
print(f"Discounted price: {discounted_price:.2f}")  # 90.00

electronic = ElectronicProduct("Laptop", 1000, "2 years")
print(f"Laptop total price: {electronic.total_price():.2f}")  # 1250.00 + 20 = 1270.00

# --- Inheritance with Property Decorators ---

class Person:
    """Base class representing a person."""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        """Get the person's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set the person's name."""
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def age(self):
        """Get the person's age."""
        return self._age

    @age.setter
    def age(self, value):
        """Set the person's age."""
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

class Employee(Person):
    """Derived class representing an employee."""

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
        self._salary = 0

    @property
    def salary(self):
        """Get the employee's salary."""
        return self._salary

    @salary.setter
    def salary(self, value):
        """Set the employee's salary."""
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value

    def describe(self):
        """Describe the employee."""
        return f"{self.name} (ID: {self.employee_id}) is {self.age} years old with a salary of {self.salary}."

print("\n--- Inheritance with Property Decorators Example ---")
employee = Employee("Kay", 39, "E12345")
employee.salary = 75000
print(employee.describe())  # Kay (ID: E12345) is 39 years old with a salary of 75000.

try:
    employee.age = -5  # This will raise ValueError
except ValueError as e:
    print(f"Error: {e}")  # Error: Age cannot be negative.

# --- Practical Example: Inheritance in a Game ---

class GameCharacter:
    """Base class representing a game character."""

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        """Attack another character."""
        damage = 10
        target.health -= damage
        return f"{self.name} attacks {target.name} for {damage} damage!"

    def __str__(self):
        return f"{self.name} (Health: {self.health})"

class Warrior(GameCharacter):
    """Derived class representing a warrior."""

    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self, target):
        """Override attack method for Warrior."""
        damage = 20  # Warriors do more damage
        target.health -= damage
        return f"{self.name} attacks {target.name} with {self.weapon} for {damage} damage!"

    def special_attack(self, target):
        """Special attack for Warrior."""
        damage = 30
        target.health -= damage
        return f"{self.name} uses special attack on {target.name} for {damage} damage!"

class Mage(GameCharacter):
    """Derived class representing a mage."""

    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def attack(self, target):
        """Override attack method for Mage."""
        damage = 15
        self.mana -= 5
        target.health -= damage
        return f"{self.name} casts a spell on {target.name} for {damage} damage!"

    def cast_spell(self, spell_name, target):
        """Cast a spell on a target."""
        damage = 25
        self.mana -= 10
        target.health -= damage
        return f"{self.name} casts {spell_name} on {target.name} for {damage} damage!"

print("\n--- Practical Example: Game Characters ---")
warrior = Warrior("Conan", 100, "Sword")
mage = Mage("Gandalf", 80, 50)
enemy = GameCharacter("Goblin", 50)

print(warrior.attack(enemy))  # Conan attacks Goblin with Sword for 20 damage!
print(mage.attack(enemy))  # Gandalf casts a spell on Goblin for 15 damage!
print(warrior.special_attack(enemy))  # Conan uses special attack on Goblin for 30 damage!
print(mage.cast_spell("Fireball", enemy))  # Gandalf casts Fireball on Goblin for 25 damage!

print(f"\n{warrior}")  # Conan (Health: 100)
print(f"{mage}")  # Gandalf (Health: 80)
print(f"{enemy}")  # Goblin (Health: -10)