#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Arguments:
    a_dictionary -- The dictionary to be printed.
    """
    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))

# Define the new_dict dictionary
new_dict = {
    "apple": 3,
    "banana": 5,
    "cherry": 1
}

# Call the function with the valid dictionary
print_sorted_dictionary(new_dict)
