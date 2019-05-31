def codes(r: int) -> list:
    """
    Given the length r, return list of all binary codes of that length.
    :param r:
    :return:
    """
    # get a list of all the ones that have length r-1
    # add 0 and 1 to each of them
    # you may want to combine using recursion along with loop

    if r == 0:
        return ['']
    L = []
    smaller = codes(r-1) # now i have a list of all the binary codes 1 smaller than the
    for code in smaller:
        L.append(code +'0')
        L.append(code + '1')
    else:
        return L

def remove_three(L):
    """use recursion. Return a new lis with all elements of L except the 3s.
    DO NOT USE ANY LIST METHODS!


    """
    if L == []:
        return []
    else:

        if L[0] == 3:
            return remove_three(L[1:])
        else:
            return [L[0]] + remove_three(L[1:])

def contains(lst: List, v: Any) -> bool:
    """return True iff lst contains value v."""
    # Do not use "in"; if lst in v, dont do that
    # use recursion
    if lst == []:
        return False
    # or return(lst[0] == v) or contains(lst[1:], v)
    elif lst[0] == v:
        return True
    else:
        return contains(lst[1:], v)

def contains2(lst, v):
    """Return true iff lst contains value v.
    lst may have nesting to arbitrary depth
    >>> contains2([1,[[2],3]],3)
    True
    """
    if lst == []:
        return False
    elif isinstance(lst[0], int):
        return lst[0] == v or contains(lst[1:], v)
    else:
        return contains2(lst[0], v) or contains(lst[1:], v)

def remove_three_sub():
    """ use recursion
    return a new list with all elements of L
    except the 3s.
    DO NOT USE ANY LIST METHODS!
    lst could be nested arbitrarily.
    >>> remove_three_sub([1, [2,3]])
    [1,[2]]
    >>> remove_three([1, [2,3], 3, [1, [3]]])
    [1, [2], 3, [1, []]]
    """
    if L == []:
        return []
    if L[0] == 3:
        return remove_three_sub()
    # for homework, will be taken up next lecture

def mystery(lst, k, value):
    """returns true if value occurs in lst at least k times.
    else returns False.
    >>> mystery([1,2,3], 2, 1)
    False
    >>> mystery([1,2,3,3], 1, 3)
    True
    """
    if len(lst) == 0:
        return k <= 0
    if lst[0] == value:
        return myster(lst[1:], k-1, value)
    else:
        return mystery(lst[1:], k, value)

