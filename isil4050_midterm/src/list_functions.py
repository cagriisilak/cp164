"""
-------------------------------------------------------
Midterm Functions
-------------------------------------------------------
Author:  Cagri Isilak
ID:      210764050
Email:   isil4050@mylaurier.ca
__updated__ = "2022-10-24"
-------------------------------------------------------
"""


def list_rotate(source, n):
    """
    -------------------------------------------------------
    Rotates position of elements in source. When finished, elements
    in source are rotated n positions to the right.
    Use: list_rotate(source, n)
    -------------------------------------------------------
    Parameters:
        source - the List to rotate (List)
        n - amount to rotate List elements (int)
    Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
        None
    -------------------------------------------------------
    """
    list = []
    num = 0
    while num < n:
        for i in source:
            list.append(i)
            source.pop(i)
        source = list
        num += 1

    return
