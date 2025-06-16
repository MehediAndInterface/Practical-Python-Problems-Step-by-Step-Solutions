

"""
Basic Arithmetic: Take two numbers as input and print their sum, difference,
product, and quotient.
1) understand the goal
2) get number from the users
3) convert input to numbers
4) perform arithmetic operations
5) handle division by zero (crucial error handling)
6) print the results
7) combine into a function
"""
def perform_arithmetic():
    # step 2 & 3: get input and covert to numbers
    try:
        # 2) get number from the users
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    print(f"Sum: {num1 + num2}")
    print(f"Difference: {num1 + num2}")
    print(f"Product: {num1 * num2}")


    # step 5 & 6
    if num2 != 0:
        quot_result = num1 / num2
    else:
        print("Cannot calculate quotient: Division by zero is not allowed.")


perform_arithmetic()






