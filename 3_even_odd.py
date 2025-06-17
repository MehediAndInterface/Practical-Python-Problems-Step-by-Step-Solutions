"""
Even or Odd: Ask the user for an integer and print whether it's even or odd.
"""

def even_odd():
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter valid integer.")
        return

    if num % 2 == 0:
        print(f"'{num}' is an even number.")
    else:
        print(f"'{num}' is an odd number")

even_odd()

