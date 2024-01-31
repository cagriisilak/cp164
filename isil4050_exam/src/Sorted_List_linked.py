"""
-------------------------------------------------------
Linked version of the Sorted_List ADT.
-------------------------------------------------------
Author: Cagri Isilak
ID:     210764050
Email:  isil4050@mylaurier.ca
__updated__ = "2022-12-14"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from copy import deepcopy



class Sorted_List:

    def has_duplicates(self):
        """
        ---------------------------------------------------------
        Determines whether source contains duplicate values.
        Use: duplicates = source.has_duplicates()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            duplicates - True if any value in this Sorted List appears more
                than once, otherwise False.
        -------------------------------------------------------
        """
        duplicates = False
        
        current = self._front
        while current is not None:
            if current._next is not None and current._value == current._next._value:
                duplicates = True

        return duplicates

    def apply(self, func):
        """
        ---------------------------------------------------------
        Returns the values where func(value) is True.
        Use: values = source.apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a node value returns
                True for some condition, otherwise returns False.
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            values - a Python list of values where func(value)
                is True (list of *)
        ----------------------------------------------------------
        """
        values = []
        current = self._front
        while current is not None:
            if current._value.apply(func) == True:
                values.append(current._value)
            current = current._next

        return values


# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            Returns the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            None
        -------------------------------------------------------
        """
        if self._front is None:
            # sorted list is empty
            node = _SL_Node(value, None)
            self._front = node
            self._rear = node
        elif value < self._front._value:
            # New value has lowest value
            self._front = _SL_Node(value, self._front)
        elif value >= self._rear._value:
            # New value has highest value
            node = _SL_Node(value, None)
            self._rear._next = node
            self._rear = node
        else:
            # Find the proper position for value.
            prev = None
            curr = self._front

            while value >= curr._value:
                prev = curr
                curr = curr._next

            # Create the new node and link it to curr.
            # The previous node is linked to the new node.
            prev._next = _SL_Node(value, curr)
        # Increment the sorted list size.
        self._count += 1
        return

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure.
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list.
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0

        while current is not None and current._value < key:
            # Take advantaged of fact the list is sorted.
            previous = current
            current = current._next
            index += 1

        if current is None or current._value != key:
            index = -1

        return previous, current, index

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _, current, i = self._linear_search(key)

        if i != -1:
            value = deepcopy(current._value)
        else:
            value = None
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        value = deepcopy(self._front._value)
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        _, _, i = self._linear_search(key)
        return i

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        _, _, i = self._linear_search(key)
        return i != -1

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_ListNode)
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return
