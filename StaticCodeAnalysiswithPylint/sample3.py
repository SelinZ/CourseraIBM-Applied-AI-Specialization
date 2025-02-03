"""Module for adding two numbers and displaying the result."""

# Constants should be in uppercase
NUM1 = 4

def add(number1: int, number2: int) -> int:
    """Return the sum of two numbers."""
    return number1 + number2


def main():
    """Main function to execute addition and print the result."""
    num2 = 5  # Variable should be lowercase
    total = add(NUM1, num2)
    print(f"The sum of {NUM1} and {num2} is {total}")


if __name__ == "__main__":
    main()
