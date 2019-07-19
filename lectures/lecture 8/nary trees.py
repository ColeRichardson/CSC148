def __len__(self) -> int:
    """
    returns the number of items contained in this tree
    >>> t1 = Tree(None, [])
    >>> len(t1)
    0
    >>> t2 = Tree(3, )
    """
    if self.Is_empty():
        return 0
    size = 1
    for child in self.children:
        size += len(child)
    return size

def count(self, item: Any):
    """return the number of occurences
    of item in this tree."""
    if self.is_empty():
        return 0
    else:
        num = 0
        if self.key == item:
            num += 1
        for child in self.children:
            num += child.count()
        return num

# Mutating methods

def delete_item(self, item: Any) -> bool:
    """
    Delete one occurnce o the given item from this tree.
    return true if item was deleted and flse otherwise
    do not modif this tree if it does not contain item.
    :param self:
    :param item:
    :return:
    """
    if self.is_empty():
    #the item is not in the tree
        return False

    elif self.key == item:
        #we've found the item: now delete it
        self._delete_root()
        return True
    else:
        #loop through each child and stop the dirst time
        # the time

def to_nested_list(self) -> List:
    """

    :param self:
    :return:
    """
    if self.is_empty():
        return []
