"""
-------------------------------------------------------
Array version of the Queue ADT.
-------------------------------------------------------
Author:  Cagri Isilak
ID:      210764050
Email:   isil4050@mylaurier.ca
__updated__ = "2022-10-25"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from copy import deepcopy



class Queue:

    def __eq__(self, target):
        """
        ----------------
        Determines whether two queues are equal.
        Entries of self and target are compared and if all contents are equal
        and in the same order, returns True, otherwise returns False.
        Use: source == target
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            equals - True if self and target are equal, False otherwise.
                source and target are unchanged. (boolean)
        ---------------
        """
        equals = False
        for i in range(len(self._values)):
            if self._values[i] == target[i]:
                equals = True
            else:
                equals = False
                break
        return equals

    # ============================================================================
    # DO NOT CHANGE code below this line.

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            the number of values in queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty queue"

        value = self._values.pop(0)
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty queue"

        value = deepcopy(self._values[0])
        return value

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in queue:
        -------------------------------------------------------
        Returns‌‌​​‌​​‌​​​​​​​​​​​‌​​​‌​​‌​:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
