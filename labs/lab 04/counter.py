class Counter:
    """A Counter, that starts counting at a certain number and 
    increments the count when requested.

    === Attributes ===
    initial: the initial value the counter began with
    current: the current value the counter is at
    increment: the value the counter increments by each time
    """
    initial: int
    current: int
    increment: int
    
    def __init__(self, init: int, inc: int) -> None:
        """Initialize a new counter with the given <init> as initial number, 
        and <inc> as increment value.
        """

        # YOUR CODE HERE
        pass


    def count(self) -> None:
        """Increment the current count by the increment value.

        >>> c = Counter(10, 2)
        >>> c.count()
        >>> c.current
        12
        """

        # YOUR CODE HERE
        pass        
        
        
    def reset(self) -> None:
        """Reset the current value to be the same as the initial value
        this counter started with.
        
        >>> c = Counter(10, 2)
        >>> c.count()
        >>> c.count()
        >>> c.current
        14
        >>> c.reset()
        >>> c.current
        10
        """

        # YOUR CODE HERE
        pass

    def change_incrementor(self, new_inc: int) -> None:
        """Update this counter's increment value to <new_inc>.

        >>> c = Counter(10, 2)
        >>> c.change_incrementor(5)
        >>> c.increment
        5
        """
        
        old_current = self.current
        old_initial = self.initial
        self = Counter(old_current, new_inc)
        self.initial = old_initial

        
