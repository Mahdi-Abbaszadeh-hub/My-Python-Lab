def classify_numbers(numbers):
    """
    Classify each number in a list as 'big' or 'small'.

    A number greater than 10 is classified as 'big', otherwise 'small'.

    Args:
        numbers (list[int | float]): A list of numeric values.

    Returns:
        list[str]: A list of classification labels ('big' or 'small').

    Example:
        >>> classify_numbers([10, 11, 8, 6, 100, 7, 9, 21])
        ['small', 'big', 'small', 'small', 'big', 'small', 'small', 'big']
    """
    return list(map(lambda n: "big" if n > 10 else "small", numbers))


# --- Usage classify_numbers ---

scores = [10, 11, 8, 6, 100, 7, 9, 21]
print(classify_numbers(scores))