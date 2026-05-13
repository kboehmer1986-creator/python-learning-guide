# This file demonstrates Object-Oriented Programming ( OOP ) in Python with classes.

# --- Basic Class Definition ---

class Dog:
    """A simple class representing a dog."""

    # Class attribute ( shared by all instances )
    
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
        return f"{self.name} the {self.color} bul