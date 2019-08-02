"""CSC148 Lab 3: Abstract Data Types

=== CSC148 Summer 2019 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga
"""
from typing import Any, List, Optional

class Queue:
    """A first-in-first-out (FIFO) queue of items.

    Stores data in a first-in, first-out order. When removing an item from the
    queue, the most recently-added item is the one that is removed.
    """
    # === Private attributes ===
    # _items: a list of the items in this queue
    _items: List

    def __init__(self) -> None:
        """Initialize a new empty queue."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this queue contains no items.

        >>> q = Queue()
        >>> q.is_empty()
        True
        >>> q.enqueue('hello')
        >>> q.is_empty()
        False
        """
        return self._items == []

    def enqueue(self, item: Any) -> None:
        """Add <item> to the back of this queue.
        """
        self._items.append(item)

    def dequeue(self) -> Optional[Any]:
        """Remove and return the item at the front of this queue.

        Return None if this Queue is empty.
        (We illustrate a different mechanism for handling an erroneous case.)

        >>> q = Queue()
        >>> q.enqueue('hello')
        >>> q.enqueue('goodbye')
        >>> q.dequeue()
        'hello'
        """
        if self.is_empty():
            return None
        else:
            return self._items.pop(0)

# TO DO: COMPLETE THE FUNCTIONS BELOW
def product(integer_queue: Queue) -> int:
    """Return the product of integers in the queue.

    Remove all items from the queue.

    Precondition: integer_queue contains only integers.

    >>> q = Queue()
    >>> q.enqueue(2)
    >>> q.enqueue(4)
    >>> q.enqueue(6)
    >>> product(q)
    48
    >>> q.is_empty()
    True
    """

    product = 1
    while not integer_queue.is_empty():
        item = integer_queue.dequeue()
        product *= item
    return product



def product_star(integer_queue: Queue) -> int:
    """Return the product of integers in the queue.

    Precondition: integer_queue contains only integers.

    >>> primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> prime_line = Queue()
    >>> for prime in primes:
    ...     prime_line.enqueue(prime)
    ...
    >>> product_star(prime_line)
    6469693230
    >>> prime_line.is_empty()
    False
    """
    q1 = Queue()
    product = 1
    while not integer_queue.is_empty():
        item = integer_queue.dequeue()
        product *= item
        q1.enqueue(item)
    while not q1.is_empty():
        integer_queue.enqueue(q1.dequeue())






    copy_queue = Queue()
    product = 1
    while not integer_queue.is_empty():
        item = integer_queue.dequeue()
        copy_queue.enqueue(item)
        product *= item
    while not copy_queue.is_empty():
        item = copy_queue.dequeue()
        integer_queue.enqueue(item)
    return product

def list_queue(q: Queue, lst: List):
    """
    >>> q = Queue()
    >>> lst = [1, 3, 5]
    >>> list_queue(q, lst)
    1
    3
    5
    >>> lst = [1, [3, 5], 7]
    >>> list_queue(q, lst)
    1
    7
    3
    5
    >>> lst = [1, [3, [5, 7], 9], 11]
    >>> list_queue(q, lst)
    1
    11
    3
    9
    5
    7
    """

    for item in lst:
        q.enqueue(item)
    while not q.is_empty():
        item1 = q.dequeue()
        if not isinstance(item1, list):
            print(item1)
        else:
            for elem in item1:
                q.enqueue(elem)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
