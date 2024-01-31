"""
-------------------------------------------------------
Exam: Simple BST testing
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2022-12-14"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST


# Constants
VALUES = [11, 7, 6, 9, 8, 15, 12, 18]
SEP = '-' * 60


def test_average_height():
    """
    Tests the 'average_height' method.
    """
    print(SEP)
    print("Test 'average_height'")
    print()
    bst = BST()
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Average Height: {bst.average_height()}")
    print()

    bst.insert(VALUES[0])
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Average Height: {bst.average_height()}")
    print()

    for v in VALUES[1:]:
        bst.insert(v)
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Average Height: {bst.average_height()}")


def test_furthest():
    """
    Tests the 'furthest' method.
    """
    print(SEP)
    print("Test 'furthest'")
    print()
    bst = BST()

    print(f"  Preorder: {bst.preorder()}")
    print(f"  Furthest: {bst.furthest()}")
    print()

    bst.insert(VALUES[0])
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Furthest: {bst.furthest()}")
    print()

    for v in VALUES[1:]:
        bst.insert(v)
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Furthest: {bst.furthest()}")


def test_is_balanced():
    """
    Tests the 'is_balanced' method.
    """
    print(SEP)
    print("Test 'is_balanced'")
    print()
    bst = BST()

    print(f"  Preorder: {bst.preorder()}")
    print(f"  Is Balanced: {bst.is_balanced()}")
    print()

    bst.insert(VALUES[0])
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Is Balanced: {bst.is_balanced()}")
    print()

    for v in VALUES[1:]:
        bst.insert(v)
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Is Balanced: {bst.is_balanced()}")
    print()

    bst = BST()
    for v in list(range(5)):
        bst.insert(v)
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Is Balanced: {bst.is_balanced()}")


if __name__ == "__main__":
    print("BST_linked Testing")
    test_average_height()
    test_furthest()
    test_is_balanced()
