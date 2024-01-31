"""
-------------------------------------------------------
Simple midterm function testing
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-10-24"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from random import shuffle

from List_array import List
from Priority_Queue_array import Priority_Queue
from Queue_array import Queue
from list_functions import list_rotate
from pq_functions import pq_strip_key
#from queue_functions import queue_split_apply
from stack_functions import check_parentheses


# Constants
SEP = "-" * 60
SIZE = 6


def is_five(n):
    return n == 5


def test_check_parentheses():
    CASES = ('none', '(x)', '((', '))', '((x)', 'x)x(x')
    print(SEP)
    print("Testing 'check_parentheses'")
    print()
    for case in CASES:
        result = check_parentheses(case)
        print(f'check_parentheses("{case}"): {result}')
    print()
    return


#def test_queue_split_apply():
 #   CASES = ([1, 2, 3, 4], [5, 5, 5, 5], [1, 5, 2, 5, 3])
  #  print(SEP)
  #  print("Testing 'queue_split_apply'")
  #  print()

    #for case in CASES:
     #   source = Queue()
      #  for v in case:
       #     source.insert(v)
        #target1, target2 = queue_split_apply(source, is_five)
        #print(
        #    f'queue_split_apply({case}, is_five): {target1._values}, {target2._values}')
    #print()
    #return


def test_split_apply():
    CASES = ([1, 2, 3, 4], [5, 5, 5, 5], [1, 5, 2, 5, 3])
    print(SEP)
    print("Testing 'split_apply'")
    print()

    for case in CASES:
        source = Queue()
        for v in case:
            source.insert(v)
        target1, target2 = source.split_apply(is_five)
        print(
            f'{case}: source.split_apply(is_five): {target1._values}, {target2._values}')
    print()
    return


def test_list_rotate():
    CASES = (0, SIZE, 1, -1, SIZE // 2,)
    print(SEP)
    print("Testing 'list_rotate'")
    print()
    values = list(range(SIZE))

    for case in CASES:
        source = List()

        for v in values:
            source.append(v)
        list_rotate(source, case)
        print(f"list_rotate({values}, {case}): {source._values}")
    print()
    return


def test_rotate():
    CASES = (0, SIZE, 1, -1, SIZE // 2,)
    print(SEP)
    print("Testing 'list_rotate'")
    print()
    values = list(range(SIZE))

    for case in CASES:
        source = List()

        for v in values:
            source.append(v)
        source.rotate(case)
        print(f"{values}: source.rotate({case}): {source._values}")
    print()
    return


def test_pq_strip_key():
    CASES = (SIZE, 0, -1, 2)
    print(SEP)
    print("Testing 'pq_strip_key'")
    print()
    values = list(range(SIZE))
    shuffle(values)

    for case in CASES:
        source = Priority_Queue()

        for v in values:
            source.insert(v)
        pq_strip_key(source, case)
        print(f"pq_strip_key({values}, {case}): {source._values}")
    print()
    return


def test_strip_key():
    CASES = (SIZE, 0, -1, 2)
    print(SEP)
    print("Testing 'strip_key'")
    print()
    values = list(range(SIZE))
    shuffle(values)

    for case in CASES:
        source = Priority_Queue()

        for v in values:
            source.insert(v)
        source.strip_key(case)
        print(f"{values}: source.strip_key({case}): {source._values}")
    print()
    return


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    test_check_parentheses()
    #test_queue_split_apply()
    #test_split_apply()
    test_list_rotate()
    test_rotate()
    test_pq_strip_key()
    test_strip_key()
