"""Temperature Converter: Convert a temperature from Celsius to Fahrenheit and
vice versa.
formula: fahrenheit = (celsius * 9/5) + 32

# 1. getting user input for temperature
# 2. converting input to a number
# 3. basic error handling for non-numeric input
# 4. implementing the conversion formula
# 5. combining everything for one conversion
# 6. adding a lopp for multiple conversions and choice
"""


def temp_conv():
    while True:
        print("\nTemperature Converter:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3):")

        if choice == '1':
            try:
                temp_cel = float(input("Enter temperature in Celsius: "))
                temp_fah = (temp_cel * 9 / 5) + 32
                print(f"{temp_cel}°C is equal to {temp_fah}°F")
            except ValueError:
                print("Invalid input. Please enter a numeric value for temperature.")
        elif choice == '2':
            try:
                temp_fah = float(input("Enter temperature in Fahrenheit: "))
                temp_cel = (temp_fah - 32) * 5 / 9
                print(f"{temp_fah}°F is equal to {temp_cel: .2f}°C")
            except ValueError:
                print("Invalid input. Please enter a numeric value for temperature.")
        elif choice == '3':
            print("Exiting Temperature Converter. Goodbye!")
            break


temp_conv()
