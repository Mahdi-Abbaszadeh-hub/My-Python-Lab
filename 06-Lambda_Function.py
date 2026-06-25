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

#----------------------------------

def get_decimal_numbers(numbers):
    """
    Filters the input list to keep only the floating-point numbers.
    
    Args:
        numbers (list): A list containing integers and floats.
        
    Returns:
        list: A list containing only numbers with a decimal part.
    """
    # Using lambda to check if the number is not equal to its integer version
    return list(filter(lambda x: x != int(x), numbers))

# --- Usage get decimal numbers ---

a = [1, 2, 3, 1.1, 2.3, 5.1]
print(get_decimal_numbers(a))

#----------------------------------

def get_short_names(names):
    """
    Filters the list to keep only names with less than 4 characters.
    
    Args:
        names (list): A list of strings (names).
        
    Returns:
        list: A list of names that have a length of 3 or less.
    """
    # Using lambda to check if the length of the string is less than 4
    short_names = filter(lambda x: len(x) < 4, names)
    return list(short_names)

# --- Usage get short names ---

a = ["mahdi", "ali", "hossin"]
print(get_short_names(a))

#----------------------------------

a = [10, 11, 8, 6, 100, 7, 9, 21]

"""
One-liner to classify numbers in a list based on a threshold.

Logic:
For each element 'x' in the list 'a':
- If x > 10, return the string 'big'.
- Else, return the string 'small'.

The 'map' function applies this lambda logic to every item in the iterable.
"""

# The one-liner magic:
print(list(map(lambda x: 'big' if x > 10 else 'small', a)))
