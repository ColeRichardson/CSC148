from __future__ import annotations
from typing import Any, List


class Node:
    """A node in a linked list.

    === Attributes ===
    item: Any
        The data stored in this node.
    next: Optional[Node]
        The next node in the list, or None if there are
        no more nodes in the list.
    """

    def __init__(self, item: Any, next_node: Optional[Node] = None) -> None:
        """Create Node self with data value and successor next.
        """

        self.item = item
        self.next = next_node  # By default, this would be None

    def __repr__(self) -> str:
        """Return a detailed str representation of Node.
        """
        if not self.next:
            return 'Node({})'.format(repr(self.item))
        else:
            return 'Node({}, {})'.format(repr(self.item), repr(
                self.next))  # This is recursive; take a few moments to think about how this works


class LinkedList:
    """A linked list implementation of the List ADT.

    === Private Attributes ===
    _first: Node or None
        The first node in the list, or None if the list is empty.
    """

    def __init__(self, items: List) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if len(items) == 0:  # No items, and an empty list!
            self._first = None
        else:
            self._first = Node(items[0])
            current_node = self._first
            for item in items[1:]:
                current_node.next = Node(item)
                current_node = current_node.next

    # ------------------------------------------------------------------------
    # Non-mutating methods: these methods do not change the list
    # ------------------------------------------------------------------------
    def __str__(self) -> str:
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

    def __getitem__(self, index: int) -> Any:
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
        """
        Append Node with <item> to the end of this list.
        """

        new_node = Node(item)

        # add this new node to the END of the list
        # you only have access to the self._first node
        # but each node has a .next

        # iterate through the list:
        if self._first is None:
            self._first = new_node
        else:
            current = self._first
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, item: Any) -> None:
        """Prepend Node with <item> to the beginning of this list.
        """

        # add this node to the BEGINNING of the list
        # make sure you don't lose any of the existing list items

        # Solution 1:
        new_node = Node(item)
        new_node.next = self._first
        self._first = new_node

        # Solution 2 (alternative solution):
        # new_node = Node(item)
        # old_head = self._first
        # self._first = new_node
        # self._first.next = old_head

        # Solution 3 (alternative solution):
        # self._first = Node(item, self._first)


from __future__ import annotations
from typing import Any, List


class Node:
    """A node in a linked list.

    === Attributes ===
    item: Any
        The data stored in this node.
    next: Optional[Node]
        The next node in the list, or None if there are
        no more nodes in the list.
    """

    def __init__(self, item: Any, next_node: Optional[Node] = None) -> None:
        """Create Node self with data value and successor next.
        """

        self.item = item
        self.next = next_node  # By default, this would be None

    def __repr__(self) -> str:
        """Return a detailed str representation of Node.
        """
        if not self.next:
            return 'Node({})'.format(repr(self.item))
        else:
            return 'Node({}, {})'.format(repr(self.item), repr(
                self.next))  # This is recursive; take a few moments to think about how this works


class LinkedList:
    """A linked list implementation of the List ADT.

    === Private Attributes ===
    _first: Optional[Node]
        The first node in the list, or None if the list is empty.
    _last: Optional[Node]
        The last node in the list, or None if the list is empty.
    """

    def __init__(self, items: List) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if len(items) == 0:  # No items, and an empty list!
            self._first = None
            self._last = None
        else:
            self._first = Node(items[0])
            current_node = self._first
            for item in items[1:]:
                current_node.next = Node(item)
                current_node = current_node.next
            self._last = current_node

    # ------------------------------------------------------------------------
    # Non-mutating methods: these methods do not change the list
    # ------------------------------------------------------------------------

    def is_empty(self) -> bool:
        """Return whether this linked list is empty.
        """

        return self._first is None

    def __str__(self) -> str:
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

    def __getitem__(self, index: int) -> Any:
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
        """
        Append Node with <item> to the end of this list.
        """

        # add this new node to the END of the list
        # in this modified linked list version, you have access to the
        # last node through the self._last attribute

        new_node = Node(item)

        if self.is_empty():
            self._first = self._last = new_node
        else:
            self._last.next = new_node
            self._last = self._last.next

    # EXERCISE: Modify this to work with the version of linked list
    # that has ._last attribute as well
    def prepend(self, item: Any) -> None:
        """Prepend Node with <item> to the beginning of this list.
        """

        # add this node to the BEGINNING of the list
        # make sure you don't lose any of the existing list items

        new_node = Node(item)
        if self.is_empty():
            self._first = self._last = new_node
        else:
            new_node.next = self._first
            self._first = new_node












