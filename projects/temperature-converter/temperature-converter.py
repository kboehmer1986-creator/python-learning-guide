# This program converts temperatures between Celsius, Fahrenheit, and Kelvin.
# It includes interactive and batch conversion modes.

import sys
from typing import List, Union, Tuple

class TemperatureConverter:
    """
    A class to handle temperature conversions between Celsius, Fahrenheit, and Kelvin.
    """

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Convert temperature from Celsius to Fahrenheit.

        Args:
            celsius (float): Temperature in Celsius.

        Returns:
            float: Temperature in Fahrenheit.
        """
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """
        Convert temperature from Fahrenheit to Celsius.

        Args:
            fahrenheit (float): Temperature in Fahrenheit.

        Returns:
            float: Temperature in Celsius.
        """
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """
        Convert temperature from Celsius to Kelvin.

        Args:
            celsius (float): Temperature in Celsius.

        Returns:
            float: Temperature in Kelvin.
        """
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """
        Convert temperature from Kelvin to Celsius.

        Args:
            kelvin (float): Temperature in Kelvin.

        Returns:
            float: Temperature in Celsius.
        """
        return kelvin - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit: float) -> float:
        """
        Convert temperature from Fahrenheit to Kelvin.

        Args:
            fahrenheit (float): Temperature in Fahrenheit.

        Returns:
            float: Temperature in Kelvin.
        """
        return TemperatureConverter.celsius_to_kelvin(
            TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        )

    @staticmethod
    def kelvin_to_fahrenheit(kelvin: float) -> float:
        """
        Convert temperature from Kelvin to Fahrenheit.

        Args:
            kelvin (float): Temperature in Kelvin.

        Returns:
            float: Temperature in Fahrenheit.
        """
        return TemperatureConverter.celsius_to_fahrenheit(
            TemperatureConverter.kelvin_to_celsius(kelvin)
        )

    @staticmethod
    def validate_temperature(value: float, unit: str) -> bool:
        """
        Validate that a temperature is physically possible.

        Args:
            value (float): Temperature value to validate.
            unit (str): Unit of the temperature ('C', 'F', or 'K').

        Returns:
            bool: True if temperature is valid, False otherwise.
        """
        unit = unit.upper()
        if unit == 'K' and value < 0:
            return False
        elif unit == 'C' and value < -273.15:
            return False
        elif unit == 'F' and value < -459.67:
            return False
        return True

    @classmethod
    def convert(cls, value: float, from_unit: str, to_unit: str) -> Union[float, None]:
        """
        Convert temperature from one unit to another.

        Args:
            value (float): Temperature value to convert.
            from_unit (str): Unit to convert from ('C', 'F', or 'K').
            to_unit (str): Unit to convert to ('C', 'F', or 'K').

        Returns:
            Union[float, None]: Converted temperature or None if invalid.
        """
        from_unit = from_unit.upper()
        to_unit = to_unit.upper()

        if from_unit == to_unit:
            return value

        if not cls.validate_temperature(value, from_unit):
            print(f"Error: Temperature {value}°{from_unit} is not physically possible.")
            return None

        conversion_functions = {
            ('C', 'F'): cls.celsius_to_fahrenheit,
            ('F', 'C'): cls.fahrenheit_to_celsius,
            ('C', 'K'): cls.celsius_to_kelvin,
            ('K', 'C'): cls.kelvin_to_celsius,
            ('F', 'K'): cls.fahrenheit_to_kelvin,
            ('K', 'F'): cls.kelvin_to_fahrenheit
        }

        key = (from_unit, to_unit)
        if key in conversion_functions:
            return conversion_functions[key](value)
        else:
            print(f"Error: Conversion from {from_unit} to {to_unit} is not supported.")
            return None

def display_menu() -> None:
    """Display the conversion menu."""
    print("\nTemperature Converter Menu:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Batch Conversion")
    print("8. Display Conversion Table")
    print("9. Exit")

def get_temperature_input(prompt: str) -> Union[float, None]:
    """
    Get temperature input from the user with validation.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        Union[float, None]: Validated temperature value or None.
    """
    while True:
        try:
            temp = float(input(prompt))
            return temp
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return None

def interactive_mode() -> None:
    """Run the temperature converter in interactive mode."""
    converter = TemperatureConverter()
    print("Welcome to the Temperature Converter!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            # Celsius to Fahrenheit
            celsius = get_temperature_input("Enter temperature in Celsius: ")
            if celsius is not None:
                fahrenheit = converter.celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C = {fahrenheit:.2f}°F")

        elif choice == '2':
            # Fahrenheit to Celsius
            fahrenheit = get_temperature_input("Enter temperature in Fahrenheit: ")
            if fahrenheit is not None:
                celsius = converter.fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F = {celsius:.2f}°C")

        elif choice == '3':
            # Celsius to Kelvin
            celsius = get_temperature_input("Enter temperature in Celsius: ")
            if celsius is not None:
                kelvin = converter.celsius_to_kelvin(celsius)
                print(f"{celsius}°C = {kelvin:.2f}K")

        elif choice == '4':
            # Kelvin to Celsius
            kelvin = get_temperature_input("Enter temperature in Kelvin: ")
            if kelvin is not None:
                celsius = converter.kelvin_to_celsius(kelvin)
                print(f"{kelvin}K = {celsius:.2f}°C")

        elif choice == '5':
            # Fahrenheit to Kelvin
            fahrenheit = get_temperature_input("Enter temperature in Fahrenheit: ")
            if fahrenheit is not None:
                kelvin = converter.fahrenheit_to_kelvin(fahrenheit)
                print(f"{fahrenheit}°F = {kelvin:.2f}K")

        elif choice == '6':
            # Kelvin to Fahrenheit
            kelvin = get_temperature_input("Enter temperature in Kelvin: ")
            if kelvin is not None:
                fahrenheit = converter.kelvin_to_fahrenheit(kelvin)
                print(f"{kelvin}K = {fahrenheit:.2f}°F")

        elif choice == '7':
            # Batch Conversion
            batch_conversion_mode()

        elif choice == '8':
            # Display Conversion Table
            display_conversion_table()

        elif choice == '9':
            # Exit
            print("Thank you for using the Temperature Converter. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

def batch_conversion_mode() -> None:
    """Run batch conversion mode."""
    converter = TemperatureConverter()

    print("\nBatch Temperature Conversion")
    print("Enter temperatures separated by spaces (e.g., 0 100 37):")

    temps_input = input("Temperatures: ").strip()
    try:
        temperatures = [float(t) for t in temps_input.split()]
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
        return

    from_unit = input("From unit (C/F/K): ").strip().upper()
    to_unit = input("To unit (C/F/K): ").strip().upper()

    if from_unit not in ['C', 'F', 'K'] or to_unit not in ['C', 'F', 'K']:
        print("Invalid units. Use 'C', 'F', or 'K'.")
        return

    print("\nConverted temperatures:")
    for original in temperatures:
        converted = converter.convert(original, from_unit, to_unit)
        if converted is not None:
            print(f"{original}°{from_unit} = {converted:.2f}°{to_unit}")

def display_conversion_table() -> None:
    """Display a temperature conversion table."""
    converter = TemperatureConverter()

    print("\nTemperature Conversion Table")
    print("°C\t°F\t\tK")
    print("-" * 30)

    for c in range(-20, 41, 10):
        f = converter.celsius_to_fahrenheit(c)
        k = converter.celsius_to_kelvin(c)
        print(f"{c:3}\t{f:5.1f}\t\t{k:5.1f}")

def command_line_mode() -> None:
    """Run the temperature converter in command-line mode."""
    if len(sys.argv) != 4:
        print("Usage: python temperature_converter.py <value> <from_unit> <to_unit>")
        print("Example: python temperature_converter.py 100 C F")
        print("Supported units: C (Celsius), F (Fahrenheit), K (Kelvin)")
        return

    try:
        value = float(sys.argv[1])
        from_unit = sys.argv[2].upper()
        to_unit = sys.argv[3].upper()

        converter = TemperatureConverter()
        result = converter.convert(value, from_unit, to_unit)

        if result is not None:
            print(f"{value}°{from_unit} = {result:.2f}°{to_unit}")
        else:
            sys.exit(1)

    except ValueError:
        print("Error: First argument must be a number.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main() -> None:
    """Main function to run the temperature converter."""
    if len(sys.argv) > 1:
        # Command-line mode
        command_line_mode()
    else:
        # Interactive mode
        interactive_mode()

if __name__ == "__main__":
    main()
