# Temperature Converter: Celsius to Fahrenheit
def convert_temperature():
    try:
        celsius = float(input("Enter Temperature: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit}°F")
    except ValueError:
        print("Please enter a valid number.")

# Run the program
convert_temperature()