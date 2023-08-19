#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
 * [6-print_sorted_dictionary.py](./6-print_sorted_dictionary.py): Python function that
  prints a dictionary by ordered keys.
  * The function assumes all keys are strings.
  * Keys are printed in alphabetic order.
  * Keys are only sorted on the first level.
  * Dictionary values can have any type.
  * Without importing modules.
