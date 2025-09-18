def avg_yield_per_acre(total_yield: float, acres: float) -> float:
    """
    Calculate the average crop yield per acre.

    Parameters:
        total_yield (float): The total crop yield (e.g., in bushels, kg, etc.).
        acres (float): The number of acres of land used for cultivation.

    Returns:
        float: The average yield per acre.

    Raises:
        ZeroDivisionError: If `acres` is zero.
        TypeError: If inputs are not numeric.

    Examples:
        >>> avg_yield_per_acre(500, 50)
        10.0

        >>> avg_yield_per_acre(300.0, 75.0)
        4.0

    Notes:
        - Ensure that both `total_yield` and `acres` are numeric (int or float).
        - If `acres` is zero, the function will raise a ZeroDivisionError.
    """
    return total_yield / acres
print(avg_yield_per_acre(500, 50))  # Output: 10.0
