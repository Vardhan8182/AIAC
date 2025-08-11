def is_palindrome(number):
    """
    Checks whether the given number is a palindrome.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    num_str = str(number)
    return num_str == num_str[::-1]