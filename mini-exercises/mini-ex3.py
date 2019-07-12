"""Mini-Exercise 3: Recursive Linked Lists

=== CSC148 Summer 2019 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module contains an incomplete implementation of a recursive linked list
class. In this example, there is no separate Node class. The LinkedList itself
acts like a Node. So we call the class a LinkedListNode.
"""

from __future__ import annotations
from typing import Any, List


class LinkedListNode:

    def __init__(self, items: List = []) -> None:
        """
        Create a new linked list containing the elements in items.
        If items is empty, self.first initialized to EmptyValue.
        """

        if len(items) == 0:  # base case: empty list
            self.first = None
        elif len(items) == 1:
            self.first = items[0]
            self.next = None
        else:
            self.first = items[0]  # initializes first item
            self.next = LinkedListNode(
                items[1:])  # creates new list with rest of items

        # NOTE ABOUT ABOVE:
        # We are recursively calling the LinkedListNode constructor in the last line
        # This is because the rest of the list should also be a LinkedListNode itself
        # So now if items = [1, 2, 3], we will end up with something like:
        #     LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, None)))
        # Key idea here:
        # The recursive structure of the LinkedList comes from thinking of the
        # list as a list of the first element, followed by a smaller LinkedList
        # of the rest of the elements
        #   LinkedList = first + smaller LinkedList of rest

    def __repr__(self) -> str:
        """
        Return a detailed str representation of Node.
        """

        if not self.next:
            return '({})'.format(repr(self.first))
        else:
            return '({}, {})'.format(repr(self.first), repr(self.next))
            # The above line is recursive; take a few moments to think about how this works

    def __str__(self) -> str:
        """
        Return a detailed str representation of Node.
        """

        return '{} -> {}'.format(str(self.first), str(self.next))
        # The above line is recursive; take a few moments to think about how this works

    def is_empty(self) -> bool:
        """
        Return True iff this list is empty.
        """

        return self.first is None

    # ============= Q1: Complete the method below =============
    def __getitem__(self, index: int) -> Any:
        """
        Return the item at position <index> in this list.
        Raise IndexError if <index> is >= the length of this list.
        >>> l0 = LinkedListNode([])
        >>> l0.__getitem__(0)
        IndexError
        >>> l1 = LinkedListNode([1,2,3])
        >>> l1.__getitem__(2)
        3
        >>> l2 = LinkedListNode([1,2,3,4])
        >>> l2.__getitem__(4)
        IndexError
        >>> l3 = LinkedListNode([1])
        >>> l3.__getitem__(0)
        1
        >>> l3.__getitem__(-1)
        IndexError
        """

        # TO DO: Complete this function recursively
        # Think about this:
        # How is finding an element at a given index in a list,
        # related to finding that index in the REST of the list?
        # e.g.
        # If we want to access the item in position 2 in the list [1,2,3,4,5],
        # how is this related to accessing an item from the rest
        # of the list, [2,3,4,5]?

        # YOUR CODE HERE
        if self.is_empty():
            raise IndexError
        elif index == 0:
            return self.first
        else:
            if self.next:
                return self.next.__getitem__(index-1)
            else:
                raise IndexError

# ==== Q2: Use the above class to complete the following function ====

def reverse_list(head: LinkedListNode) -> LinkedListNode:
    '''
    Reverse the list that starts with the given <head> as its first node,
    and return the new head of the list.

    >>> ll = LinkedListNode([1, 2, 3])
    >>> ll = reverse_list(ll)
    >>> print(ll)
    3 -> 2 -> 1 -> None
    >>> l2 = LinkedListNode([1])
    >>> l2 = reverse_list(l2)
    >>> print(l2)
    1 -> None
    >>> l3 = LinkedListNode([5, 6, 7, 8, 9, 10])
    >>> l3 = reverse_list(l3)
    >>> print(l3)
    10 -> 9 -> 8 -> 7 -> 6 -> 5 -> None
    '''

    # TO DO: Complete this function recursively
    if head.is_empty() or not head.next:
        return head

    else:
        new = head.next
        head.next = None
        new_list = reverse_list(new)
        new.next = head
        return new_list

import doctest

doctest.testmod(verbose=True)

