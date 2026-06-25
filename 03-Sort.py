"""
Sort a list of tuples by the second element.

By default, sort() orders tuples by the first element.
Using the `key` parameter lets us choose a different
value for comparison. Here we use the second element
of each tuple (x[1]) as the sorting key.
"""

# List of tuples
a = [(3, 4), (7, 1), (5, 9), (2, 2)]

# Sort the list based on the second value of each tuple
a.sort(key=lambda x: x[1])

# Print the sorted result
print(a)
