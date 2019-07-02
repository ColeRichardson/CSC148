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

    >> L = ['a', 'b', ['c', 'd', ['e']]]
    >> list_to_dict(L)
    {'0': 'a', '1': 'b', '2->0': 'c', '2->1': 'd', '2->2->0': 'e'}
    '''

    # YOUR CODE HERE
    new_dict = {}
    i = 0
    j = 0
    if not isinstance(lst[0], list):
        
        return list_to_dict(lst[1:])
        #  elif isinstance(lst[1:], list):
    #else:
    else:
        return new_dict

