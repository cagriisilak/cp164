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


def pq_strip_key(source, key):
    """
    -------------------------------------------------------
    Removes all values from source that have a priority
    less than key.
    Use: pq_strip_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a key value (?)
    Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
        None
    -------------------------------------------------------
    """

    for i in source:
        if i < key:
            source.remove(i)

    return
