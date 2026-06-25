# dict
my_dict = {"key": "value", "name": "mahdi", "famaily": "abbaszadeh"}

# if key in my_dict --> print value in my_dict
print(my_dict.get("key"))

# if key not in my_dict --> print None
print(my_dict.get("hasan"))

# How to change all key values ​​in a dictionary
# Whatever is key to the name of the name becomes Hasan.
my_dict.update({"name": "hasan"})
print(my_dict)

my_dic_2 = {"name": "mahdi", "family": "naseri", "id": 1223456}
# add key and value in dictionary
my_dic_2["age"] = 20
# change value key
my_dic_2["name"] = "hasan"
# remove key and value in dic
my_dic_2.pop("id")
print(my_dic_2)

# --------------------------

def most_frequent(elements):
    """
    Find the most frequently occurring element in a list.

    Args:
        elements (list): A list of hashable items (e.g. integers, strings).

    Returns:
        The element that appears most often in the list.

    Example:
        >>> most_frequent([1, 3, 1, 3, 2, 1])
        1
    """
    frequency = {}
    for element in elements:
        if element not in frequency:
            frequency[element] = 1
        else:
            frequency[element] += 1
    return max(frequency, key=frequency.get)

# --- Usage most_frequent ---

numbers = [1, 3, 1, 3, 2, 1]
print(most_frequent(numbers))

# --------------------------

def unique_numbers(numbers):
    """
    Identifies and extracts numbers that appear exactly once in the input list.

    This function processes the input list to determine the frequency of each 
    integer and returns a list containing only those elements that have a 
    frequency count of exactly one.

    Problem:
    Given a list of integers where some elements may be repeated, how can 
    we isolate the numbers that are strictly unique (i.e., appear only once)?

    Args:
        numbers (list[int]): A list of integers to be processed.

    Returns:
        list[int]: A list containing the integers that occurred exactly once 
                   in the input list.

    Example:
        >>> unique_numbers([1, 2, 2, 3, 4, 4, 5])
        [1, 3, 5]
    """
    my_dic = {}
    my_list = []
    for num in numbers:
        if num not in my_dic:
            my_dic[num] = 1
        else:
            my_dic[num] += 1
    for key, value in my_dic.items():
        if value == 1:
            my_list.append(key)
    return my_list

# --- Usage most_frequent ---

print(unique_numbers([1,2,2,3,4,4,5]))

# --------------------------
