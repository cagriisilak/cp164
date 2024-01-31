"""
-------------------------------------------------------
Exam: Simple Sorted List testing
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2022-12-14"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from Sorted_List_linked import Sorted_List

# Constants
VALUES = list(range(8))
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies Sorted_List values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def from_python_list(values):
    """
    Testing helper method. Copies Python list values to a Sorted_List.
    """
    source = Sorted_List()
    for value in values:
        source.insert(value)
    return source


def is_even(value):
    """
    ---------------------------------------------------------
    Determines whether an integer value is even.
    Use: values = source.apply(func)
    -------------------------------------------------------
    Parameters:
        value - an integer (int)
    Returns:
        even - True if value is even, False otherwise (bool)
    ----------------------------------------------------------
    """
    even = value % 2 == 0
    return even


def test_has_duplicates():
    """
    Tests the 'has_duplicates' method.
    """
    print(SEP)
    print("Test 'has_duplicates'")
    print()

    source = Sorted_List()
    print(f"  List: {to_python_list(source)}")
    print(f"  Has Duplicates: {source.has_duplicates()}")
    print()

    source = from_python_list(VALUES)
    print(f"  List: {to_python_list(source)}")
    print(f"  Has Duplicates: {source.has_duplicates()}")
    print()

    source = from_python_list(VALUES)
    source.insert(VALUES[-1])
    print(f"  List: {to_python_list(source)}")
    print(f"  Has Duplicates: {source.has_duplicates()}")
    print()

    source = from_python_list(VALUES)
    source.insert(VALUES[0])
    print(f"  List: {to_python_list(source)}")
    print(f"  Has Duplicates: {source.has_duplicates()}")
    print()


def test_apply():
    """
    Tests the 'apply' method.
    """
    print(SEP)
    print("Test 'apply'")
    print()

    source = Sorted_List()
    print(f"  List: {to_python_list(source)}")
    print(f"  Even values: {source.apply(is_even)}")
    print()

    source = from_python_list(VALUES)
    print(f"  List: {to_python_list(source)}")
    print(f"  Even values: {source.apply(is_even)}")
    print()

    source = from_python_list(VALUES)
    source.insert(VALUES[-1])
    print(f"  List: {to_python_list(source)}")
    print(f"  Even values: {source.apply(is_even)}")
    print()

    source = from_python_list(VALUES)
    source.insert(VALUES[0])
    print(f"  List: {to_python_list(source)}")
    print(f"  Even values: {source.apply(is_even)}")
    print()


if __name__ == "__main__":
    print("Sorted_List_linked Testing")
    test_has_duplicates()
    test_apply()
