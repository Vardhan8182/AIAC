def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using an iterative approach.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

    # Example usage of the factorial function
if __name__ == "__main__":
    num = int(input("Enter a non-negative integer: "))
    try:
        print(f"Factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print(e)


        def get_factorial_from_user():
            """
            Prompts the user to enter a non-negative integer and prints its factorial.
            """
            try:
                num = int(input("Enter a non-negative integer: "))
                print(f"Factorial of {num} is {factorial(num)}")
            except ValueError as e:
                print(f"Invalid input: {e}")


                def generate_factorial_from_console():
                    """
                    Prompts the user to enter a non-negative integer and prints its factorial.
                    """
                    try:
                        n = int(input("Enter a non-negative integer: "))
                        print(f"Factorial of {n} is {factorial(n)}")
                    except ValueError as e:
                        print(f"Invalid input: {e}")
