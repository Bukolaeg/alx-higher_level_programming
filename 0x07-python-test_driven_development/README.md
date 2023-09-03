# Project Title: Test-driven Development Practice in Python

In this project, I've been practicing test-driven development (TDD) using `docstrings` and `unittest` in Python.

## Tests :heavy_check_mark:

* [tests](./tests): This folder contains both Holberton-provided test files and additional independently-developed test cases.

### Independently-Developed Test Files
  * [0-add_integer.txt](./tests/0-add_integer.txt)
  * [2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  * [3-say_my_name.txt](./tests/3-say_my_name.txt)
  * [4-print_square.txt](./tests/4-print_square.txt)
  * [5-text_indentation.txt](./tests/text_indentation.txt)
  * [6-max_integer_test.py](./tests/6-max_integer_test.py)
  * [100-matrix_mul.txt](./tests/100-matrix_mul.txt)
  * [101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)

## Function Prototypes :floppy_disk:

Here are the prototypes for the functions developed in this project:

| File                     | Prototype                                    |
| ------------------------ | -------------------------------------------- |
| `0-add_integer.py`       | `def add_integer(a, b=98):`                  |
| `2-matrix_divided.py`    | `def matrix_divided(matrix, div):`           |
| `3-say_my_name.py`       | `def say_my_name(first_name, last_name=""):` |
| `4-print_square.py`      | `def print_square(size):`                    |
| `5-text_indentation.py`  | `def text_indentation(text):`                |
| `100-matrix_mul.py`      | `def matrix_mul(m_a, m_b):`                  |
| `101-lazy_matrix_mul.py` | `def lazy_matrix_mul(m_a, m_b):`             |
| `102-python.c`           | `void print_python_string(PyObject *p);`     |

## Tasks :page_with_curl:

Here are the tasks completed in this project:

### Task 0: Integers Addition
  * File: [0-add_integer.py](./0-add_integer.py)
  * Description: Python function that returns the integer addition of two numbers.
  * Additional Requirements:
    - If either `a` or `b` is not an `int` or `float`, a `TypeError` is raised.
    - If either `a` or `b` is a `float`, it is casted to an `int` before addition.

### Task 1: Divide a Matrix
  * File: [2-matrix_divided.py](./2-matrix_divided.py)
  * Description: Python function that divides all elements of a matrix by a common divisor.
  * Additional Requirements:
    - Returns a new matrix representing the division of all elements of `matrix` by `div`.
    - Quotients are rounded to two decimal places.
    - Various error conditions are handled, such as non-integer/divisible matrix elements, etc.

### Task 2: Say My Name
  * File: [3-say_my_name.py](./3-say_my_name.py)
  * Description: Python function that prints a name in the format `My name is <first_name> <last_name>`.
  * Additional Requirements:
    - Handles cases where `first_name` or `last_name` is not a string.

### Task 3: Print Square
  * File: [4-print_square.py](./4-print_square.py)
  * Description: Python function that prints a square using the `#` character.
  * Additional Requirements:
    - The `size` parameter represents the height/width of the square.
    - Various error conditions are handled, such as non-integer `size` and negative `size`.

### Task 4: Text Indentation
  * File: [5-text_indentation.py](./5-text_indentation.py)
  * Description: Python function that prints text with proper indentation.
  * Additional Requirements:
    - New lines are added after specific characters (`.`, `?`, `:`).
    - Handles cases where `text` is not a string.

### Task 5: Max Integer - Unittest
  * File: [tests/6-max_integer_test.py](./tests/6-max_integer_test.py)
  * Description: Python class/script that runs unittests for the function `def max_integer(list=[]):` (provided by Holberton School).

### Task 6: Matrix Multiplication
  * File: [100-matrix_mul.py](./100-matrix_mul.py)
  * Description: Python function that multiplies two matrices.
  * Additional Requirements:
    - Handles various error conditions, such as empty matrices, non-matrix inputs, and incompatible matrix dimensions.

### Task 7: Lazy Matrix Multiplication
  * File: [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py)
  * Description: Python function that multiplies two matrices using the `NumPy` library.
  * Additional Requirements:
    - Identical in function to Task 6.

### Task 8: CPython #3: Python Strings
  * File: [102-python.c](./102-python.c)
  * Description: C function that prints basic information about Python string objects.

