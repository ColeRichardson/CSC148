def list_to_dict(lst: list) -> dict:
    '''
    Given a list L that may have sublists nested within it at an arbitrary
    depth, return a dictionary that has all the values from the list as its
    values, and the associated keys for each value are the indices that
    we would need to go through to get to that value. The key is represented
    as a string as exemplified below.

    e.g. In the list shown below, the value 'a' is at L[0] so
    the key for this value in the dictionary returned is just '0'.
    The value 'd' is at index L[2][1] so the key for this value is
    '2->1'. The value 'e' is at index L[2][2][0], so the key for this
    value is '2->2->0' and so on.

    Note: Your code MUST be recursive

    >>> L = ['a', 'b', ['c', 'd', ['e']]]
    >>> list_to_dict(L)
    {'0': 'a', '1': 'b', '2->0': 'c', '2->1': 'd', '2->2->0': 'e'}
    >>> L1 = ['a', 'b', 'c', 'd']
    >>> list_to_dict(L1)
    {'0': 'a', '1': 'b', '2': 'c', '3': 'd'}
    >>> L2 = ['a',['b', 'c'], ['d', ['e', 'f']]]
    >>> list_to_dict(L2)
    {'0': 'a', '1->0': 'b', '1->1': 'c', '2->0': 'd', '2->1->0': 'e', '2->1->1': 'f'}
    '''

    enum_list = list(enumerate(lst))
    d = {}

    for elem in enum_list:
        if not isinstance(elem[1], list):
            d[str(elem[0])] = str(elem[1])
        else:
            for k, v in list_to_dict(elem[1]).items():
                d[str(elem[0]) + '->' + str(k)] = str(v)
    return d
