"""
-------------------------------------------------------
Exam: Simple List testing
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2022-12-14"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from List_linked import List

# Constants
VALUES = [3, 8, 6, 7, 6, 2, 4, 6]
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies List values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def from_python_list(values):
    """
    Testing helper method. Copies Python list values to a List.
    """
    source = List()
    for value in values:
        source.append(value)
    return source


def test_append_front():
    """
    Tests the 'append_front' method.
    """
    print(SEP)
    print("Test 'append_front'")
    print()

    source = List()
    print(f"  List: {to_python_list(source)}")
    source.append_front()
    print(f"  After 'append_front': {to_python_list(source)}")
    print()

    source = from_python_list(VALUES[:1])
    print(f"  List: {to_python_list(source)}")
    source.append_front()
    print(f"  After 'append_front': {to_python_list(source)}")
    print()

    source = from_python_list(VALUES)
    print(f"  List: {to_python_list(source)}")
    source.append_front()
    print(f"  After 'append_front': {to_python_list(source)}")
    print()


def test_prepend_rear():
    """
    Tests the 'prepend_rear' method.
    """
    print(SEP)
    print("Test 'prepend_rear'")
    print()

    source = List()
    print(f"  List: {to_python_list(source)}")
    source.prepend_rear()
    print(f"  After 'prepend_rear': {to_python_list(source)}")
    print()

    source = from_python_list(VALUES[:1])
    print(f"  List: {to_python_list(source)}")
    source.prepend_rear()
    print(f"  After 'prepend_rear': {to_python_list(source)}")
    print()

    source = from_python_list(VALUES)
    print(f"  List: {to_python_list(source)}")
    source.prepend_rear()
    print(f"  After 'prepend_rear': {to_python_list(source)}")
    print()


def test_detect_loop():
    """
    Tests the 'detect_loop' method.
    """
    print(SEP)
    print("Test 'detect_loop'")
    print()

    source = List()
    print(f"  List: {to_python_list(source)}")
    print(f"  Has Loop: {source.detect_loop()}")
    print()

    source = from_python_list(VALUES)
    print(f"  List: {to_python_list(source)}")
    print(f"  Has Loop: {source.detect_loop()}")
    print()

    print("  source._rear._next = source._rear")
    source._rear._next = source._rear
    print(f"  Has Loop: {source.detect_loop()}")
    print()

    print("  source._front._next._next._next = source._front._next")
    source._front._next._next._next = source._front._next
    print(f"  Has Loop: {source.detect_loop()}")
    print()

    print("  source._front._next = source._front")
    source._front._next = source._front
    print(f"  Has Loop: {source.detect_loop()}")
    print()


if __name__ == "__main__":
    print("List_linked Testing")
    test_append_front()
    test_prepend_rear()
    test_detect_loop()
