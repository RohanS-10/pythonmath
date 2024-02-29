import math
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def perform_calculations():
    print("Math Operations:")
    print("1. Basic Calculation")
    print("2. Solve Equation")
    print("3. Plot Function")

    choice = input("Enter the number corresponding to the desired operation: ")

    if choice == "1":
        expression = input("Enter a mathematical expression: ")
        result = eval(expression)
        print(f"Result: {result}")

    elif choice == "2":
        equation = input("Enter an equation in terms of x: ")
        x = sp.symbols('x')
        solution = sp.solve(equation, x)
        print(f"Solutions: {solution}")

    elif choice == "3":
        expression = input("Enter a function in terms of x: ")
        x_vals = np.linspace(-10, 10, 100)
        y_vals = [eval(expression) for x in x_vals]

        plt.plot(x_vals, y_vals)
        plt.title("Plot of the Function")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()

    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    print("Welcome to the Interactive Math Program!")

    while True:
        perform_calculations()

        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Exiting the program. Goodbye!")
            break
