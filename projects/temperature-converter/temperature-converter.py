# This program converts temperatures between Celsius, Fahrenheit and Kelvin.

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """
    Convert temperature from Celsius to Kelvin.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Kelvin.
    """
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.

    Args:
        kelvin (float): Temperature in Kelvin.

    Returns:
        float: Temperature in Celsius.
    """
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """
    Convert temperature from Fahrenheit to Kelvin.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Kelvin.
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    """
    Convert temperature from Kelvin to Fahrenheit.

    Args:
        kelvin (float): Temperature in Kelvin.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def display_menu():
    """Display the conversion menu."""
    print("\nTemperature Converter Menu:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

def get_temperature_input(prompt):
    """
    Get temperature input from the user with validation.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        float: The validated temperature value.
    """
    while True:
        try:
            temp = float(input(prompt))
            # Check for absolute zero violations
            if prompt.lower().find("kelvin") != -1 and temp < 0:
                print("Error: Temperature in Kelvin cannot be below 0.")
                continue
            if prompt.lower().find("celsius") != -1 and temp < -273.15:
                print("Error: Temperature in Celsius cannot be below -273.15.")
                continue
            if prompt.lower().find("fahrenheit") != -1 and temp < -459.67:
                print("Error: Temperature in Fahrenheit cannot be below -459.67.")
                continue
            return temp
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    """Main function to run the temperature converter."""
    print("Welcome to the Temperature Converter!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            # Celsius to Fahrenheit
            celsius = get_temperature_input("Enter temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit:.2f}°F")

        elif choice == '2':
            # Fahrenheit to Celsius
            fahrenheit = get_temperature_input("Enter temperature in Fahrenheit: ")
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {celsius:.2f}°C")

        elif choice == '3':
            # Celsius to Kelvin
            celsius = get_temperature_input("Enter temperature in Celsius: ")
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius}°C = {kelvin:.2f}K")

        elif choice == '4':
            # Kelvin to Celsius
            kelvin = get_temperature_input("Enter temperature in Kelvin: ")
            celsius = kelvin_to_celsius(kelvin)
            print(f"{kelvin}K = {celsius:.2f}°C")

        elif choice == '5':
            # Fahrenheit to Kelvin
            fahrenheit = get_temperature_input("Enter temperature in Fahrenheit: ")
            kelvin = fahrenheit_to_kelvin(fahrenheit)
            print(f"{fahrenheit}°F = {kelvin:.2f}K")

        elif choice == '6':
            # Kelvin to Fahrenheit
            kelvin = get_temperature_input("Enter temperature in Kelvin: ")
            fahrenheit = kelvin_to_fahrenheit(kelvin)
            print(f"{kelvin}K = {fahrenheit:.2f}°F")

        elif choice == '7':
            # Exit
            print("Thank you for using the Temperature Converter. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

def batch_convert(temperatures, from_unit, to_unit):
    """
    Convert a list of temperatures from one unit to another.

    Args:
        temperatures (list): List of temperature values.
        from_unit (str): Unit to convert from ('C', 'F', 'K').
        to_unit (str): Unit to convert to ('C', 'F', 'K').

    Returns:
        list: List of converted temperatures.
    """
    converted = []
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    for temp in temperatures:
        if from_unit == 'C' and to_unit == 'F':
            converted.append(celsius_to_fahrenheit(temp))
        elif from_unit == 'F' and to_unit == 'C':
            converted.append(fahrenheit_to_celsius(temp))
        elif from_unit == 'C' and to_unit == 'K':
            converted.append(celsius_to_kelvin(temp))
        elif from_unit == 'K' and to_unit == 'C':
            converted.append(kelvin_to_celsius(temp))
        elif from_unit == 'F' and to_unit == 'K':
            converted.append(fahrenheit_to_kelvin(temp))
        elif from_unit == 'K' and to_unit == 'F':
            converted.append(kelvin_to_fahrenheit(temp))
        else:
            raise ValueError("Invalid unit. Use 'C', 'F', or 'K'.")

    return converted

def interactive_batch_convert():
    """Interactive batch conversion."""
    print("\nBatch Temperature Conversion")
    print("Enter temperatures separated by spaces (e.g., 0 100 37):")

    temps_input = input("Temperatures: ")
    try:
        temperatures = [float(t) for t in temps_input.split()]
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
        return

    from_unit = input("From unit (C/F/K): ").upper()
    to_unit = input("To unit (C/F/K): ").upper()

    if from_unit not in ['C', 'F', 'K'] or to_unit not in ['C', 'F', 'K']:
        print("Invalid units. Use 'C', 'F', or 'K'.")
        return

    try:
        converted = batch_convert(temperatures, from_unit, to_unit)
        print("\nConverted temperatures:")
        for original, converted_temp in zip(temperatures, converted):
            print(f"{original}°{from_unit} = {converted_temp:.2f}°{to_unit}")
    except ValueError as e:
        print(f"Error: {e}")

def temperature_table():
    """Display a temperature conversion table."""
    print("\nTemperature Conversion Table")
    print("°C\t°F\tK")
    print("-" * 20)

    for c in range(-20, 41, 10):
        f = celsius_to_fahrenheit(c)
        k = celsius_to_kelvin(c)
        print(f"{c:3}\t{f:5.1f}\t{k:5.1f}")

if __name__ == "__main__":
    # Run the main interactive program
    main()

    # Uncomment the following lines to test other features:
    # interactive_batch_convert()
    # temperature_table()

    # Example of batch conversion:
    # temps = [0, 100, 37]
    # print(batch_convert(temps, 'C', 'F'))  # [32.0, 212.0, 98.6]
    # print(batch_convert(temps, 'F', 'C'))  # [-17.777..., 37.777..., -0.555...]
    # print(batch_convert(temps, 'C', 'K'))  # [273.15, 373.15, 310.15]