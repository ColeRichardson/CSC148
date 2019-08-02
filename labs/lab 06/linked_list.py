"""Lab 6: Linked List Exercises

=== Module Description ===
This module contains the code for a linked list implementation with two classes,
LinkedList and Node.

All of the code from lecture is here, as well as some exercises to work on.
"""

from __future__ import annotations
from typing import Any


class Node:
    """A node in a linked list.

    === Attributes ===
    item: object
        The data stored in this node.
    next: Node or None
        The next node in the list, or None if there are
        no more nodes in the list.
    """
    item: Any
    next: Optional[Node]

    def __init__(self: Node, item: Any,
                 next_node: Optional[Node] = None) -> None:
        """Initialize a new node storing <item>, with the given
        <next_node> as the node that follows it.
        """

        self.item = item
        self.next = next_node  # By default, this would be None

    def __repr__(self: Node) -> str:
        """Return a detailed str representation of Node.
        """

        if not self.next:
            return 'Node({})'.format(repr(self.item))
        else:
            # This is recursive; take a few moments to think about how this works
            return 'Node({}, {})'.format(repr(self.item), repr(self.next))


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first: Node or None
    #    The first node in the list, or None if the list is empty.
    _first: Optional[Node]

    def __init__(self, items: list) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if items == []:  # No items, and an empty list!
            self._first = None
        else:
            self._first = Node(items[0])
            curr = self._first
            for item in items[1:]:
                curr.next = Node(item)
                curr = curr.next

    # ------------------------------------------------------------------------
    # Non-mutating methods: these methods do not change the list
    # ------------------------------------------------------------------------
    def is_empty(self) -> bool:
        """Return whether this linked list is empty.
        """
        return self._first is None

    def __str__(self):
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> lst = LinkedList([1, 2, 3])
        >>> str(lst)
        '[1 -> 2 -> 3]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def __repr__(self) -> str:
        """Return a detailed str representation of LinkedList in the form
        LinkedList(Node(value, Node(value, ...)))

        >>> lst = LinkedList([1, 2, 3])
        >>> repr(lst)
        'LinkedList(Node(1, Node(2, Node(3))))'
        """
        if self._first is None:
            return 'LinkedList()'
        else:
            return 'LinkedList(' + repr(self._first) + ')'

    def __getitem__(self, index: int) -> object:
        """Return the item at position <index> in this list.
        Raise IndexError if <index> is >= the length of this list.
        """

        curr = self._first
        curr_index = 0

        # Iterate to (index)-th node
        while curr is not None and curr_index < index:
            curr = curr.next
            curr_index += 1

        if curr is None:
            raise IndexError
        else:
            return curr.item

    # ------------------------------------------------------------------------
    # Mutating methods: these methods do change the list
    # ------------------------------------------------------------------------

    def append(self, item: Any) -> None:
        """Append <item> to the end of this list.

        >>> lst = LinkedList([1, 2, 3])
        >>> str(lst)
        '[1 -> 2 -> 3]'
        >>> lst.append(4)
        >>> str(lst)
        '[1 -> 2 -> 3 -> 4]'
        """
        if self._first is None:
            self._first = Node(item)
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(item)

    def prepend(self, item: Any) -> None:
        """Prepend Node with <item> to the beginning of this list.
        """

        new_node = Node(item)
        curr = self._first
        if curr is None:
            self._first = new_node
        else:
            new_node.next = self._first
            self._first = new_node

    # -------------------------
    # --- Lab Exercises ---

    def __len__(self) -> int:
        """Return the number of elements in this list.

        >>> lst = LinkedList([])
        >>> len(lst)              # Equivalent to lst.__len__()
        0
        >>> lst = LinkedList([1, 2, 3])
        >>> len(lst)
        3
        """
        

    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this list.

        Use == to compare items.

        >>> lst = LinkedList([1, 2, 3])
        >>> 2 in lst                     # Equivalent to lst.__contains__(2)
        True
        >>> 4 in lst
        False
        """
        pass

    def count(self, item: Any) -> int:
        """Return the number of times <item> occurs in this list.

        Use == to compare items.

        >>> lst = LinkedList([1, 2, 1, 3, 2, 1])
        >>> lst.count(1)
        3
        >>> lst.count(2)
        2
        >>> lst.count(3)
        1
        """
        pass

    def index(self, item: Any) -> int:
        """Return the index of the first occurrence of <item> in this list.

        Raise ValueError if the <item> is not present.

        Use == to compare items.

        >>> lst = LinkedList([1, 2, 1, 3, 2, 1])
        >>> lst.index(1)
        0
        >>> lst.index(3)
        3
        """
        pass
