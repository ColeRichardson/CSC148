# Exercise 2, Task 2- A Chain of People
#
# CSC148 Summer 2019, University of Toronto
# Instructor: Sadia Sharmin
# ---------------------------------------------
"""
This module contains the following classes to represent a chain of people --
Person: a person in the chain.
PeopleChain: ordered chain consisting of people.
ShortChainError: indicates chain is too short to perform action.
"""
from __future__ import annotations


class ShortChainError(Exception):
    pass


class Person:

    def __init__(self, name, next=None):
        self.name = name
        self.next = next


class PeopleChain:
    """A chain of people.

    === Attributes ===
    leader: Person | None
        The first person in the chain, or None if the chain is empty.
    """
    leader: Optional[Person]

    def __init__(self, names: List[str]) -> None:
        """Create people linked together in the order provided in <names>.

        The leader of the chain is the first person in <names>.
        """
        if len(names) == 0:
            # No leader, representing an empty chain!
            self.leader = None
        else:
            # Set leader
            self.leader = Person(names[0])
            current_person = self.leader
            for name in names[1:]:
                # Set the link for the current person
                current_person.next = Person(name)
                # Update the current person
                # Note that current_person always refers to
                # the LAST person in the chain
                current_person = current_person.next

    # TODO: Implement the following four methods!
    def get_leader(self) -> str:
        """Return the name of the leader of the chain.

        Raise ShortChainError if chain has no leader.

        >>> chain = PeopleChain(['Iron Man', 'Heather', 'Kevan'])
        >>> chain.get_leader()
        'Iron Man'

        >>> chain = PeopleChain([])
        >>> chain.get_leader()
        Traceback (most recent call last):
        ...
        ShortChainError
        """

        # YOUR CODE HERE
        if not self.leader:
            raise ShortChainError
        else:
            return self.leader.name

    def get_second(self) -> str:
        """Return the name of the second person in the chain.

        That is, return the name of the person the leader is holding onto.
        Raise ShortChainError if chain has no second person.

        >>> chain = PeopleChain(['Iron Man', 'Heather', 'Kevan'])
        >>> chain.get_second()
        'Heather'

        >>> chain = PeopleChain(['Iron Man'])
        >>> chain.get_second()
        Traceback (most recent call last):
        ...
        ShortChainError
        """

        # YOUR CODE HERE
        if not self.leader or not self.leader.next:
            raise ShortChainError
        else:
            return self.leader.next.name

    def get_third(self) -> str:
        """Return the name of the third person in the chain.

        Raise ShortChainError if chain has no third person.

        >>> chain = PeopleChain(['Iron Man', 'Heather', 'Kevan'])
        >>> chain.get_third()
        'Kevan'

        >>> chain = PeopleChain(['Iron Man'])
        >>> chain.get_third()
        Traceback (most recent call last):
        ...
        ShortChainError
        """

        # YOUR CODE HERE
        if not self.leader or not self.leader.next or not self.leader.next.next:
            raise ShortChainError
        else:
            return self.leader.next.next.name

    def get_nth(self, n: int) -> str:
        """Return the name of the n-th person in the chain.

        Precondition: n >= 0

        Raise ShortChainError if chain doesn't have n people.

        >>> chain = PeopleChain(['Iron Man', 'Heather', 'Kevan'])
        >>> chain.get_nth(0)
        'Iron Man'

        >>> chain = PeopleChain(['Iron Man', 'Heather', 'Kevan'])
        >>> chain.get_nth(2)
        'Kevan'

        >>> chain = PeopleChain(['Iron Man', 'Heather', 'Kevan'])
        >>> chain.get_nth(5)
        Traceback (most recent call last):
        ...
        ShortChainError
        """

        # YOUR CODE HERE
        if not self.leader:
            raise ShortChainError
        elif self.leader:
            curr = self.leader
            for i in range(0, n):
                if not curr.next:
                    raise ShortChainError
                else:
                    curr = curr.next
            return curr.name


import doctest
doctest.testmod()
