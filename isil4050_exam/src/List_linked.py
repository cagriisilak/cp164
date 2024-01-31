"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author: Cagri Isilak
ID:     210764050
Email:  isil4050@mylaurier.ca
__updated__ = "2022-12-14"
-------------------------------------------------------
"""
# pylint: disable=protected-access

from copy import deepcopy


class List:

    def append_front(self):
        """
        -------------------------------------------------------
        Moves the front node to the rear of the List.
        Use: source.append_front()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            None
        -------------------------------------------------------
        """
        
        if self._front is not None and self._front._next is not None:
            next = self._front._next
            current = self._front
            while current._next is not None:
                current = current._next
            end = current
            
            self._front = next
            end._next = self._front
            self._front._next = None

        return

    def prepend_rear(self):
        """
        -------------------------------------------------------
        Moves the rear node to the front of the List.
        Use: source.prepend_rear()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            None
        -------------------------------------------------------
        """
        
        if self._front is not None and self._front._next is not None:
            current = self._front
            while current._next is not None:
                current = current._next
            end = current
            current = self._front
            while current._next is not end:
                current = current._next
            prev = current
            prev._next = None
            end._next = self._front
            self._front = end
            

        return

    def detect_loop(self):
        """
        -------------------------------------------------------
        Determines if the List contains a circular reference/loop.
        Use: circular = source.detect_loop()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            circular - True if source contains a circular reference,
                False otherwise (bool)
        -------------------------------------------------------
        """
        circular = False

        x = self._front
        y = self._front

        while y is not None and y._next is not None:
            x = x._next
            y = y._next._next

            if x is y:
                circular = True
            else:
                circular = False
            
        return circular



# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

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


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
