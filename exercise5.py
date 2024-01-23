def check_first_last(numbers):
    """
    This function checks if the first and last numbers of a list are the same.

    Args:
      numbers: A list of numbers.

    Returns:
      True if the first and last number are the same, False if otherwise.
    """
    if len(numbers) < 2:
        return False
    return numbers [0] == numbers [-1]

# Example usage
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

result_x = check_first_last(numbers_x)
result_y = check_first_last(numbers_y)

print(f"List: {numbers_x}, First and last same? {result_x}")
print(f"List: {numbers_y}, First and last same? {result_y}")