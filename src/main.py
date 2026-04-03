"""Main entry point for the CI/CD Demo Application."""

from src.math import add, subtract, multiply, divide

if __name__ == "__main__":
    print("CI/CD Demo Application")
    print(f"Addition result: {add(10, 5)}")
    print(f"Subtraction result: {subtract(10, 5)}")
    print(f"Multiplication result: {multiply(10, 5)}")
    print(f"Division result: {divide(10, 5)}")
