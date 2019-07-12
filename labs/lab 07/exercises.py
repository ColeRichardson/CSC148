from typing import List, Union


def sum_nested(obj: Union[int, List]) -> int:
    """Return the sum of the numbers in a nested list.

    Note that a obj is one of two things:
      1. a number
      2. a list of (less deep) nested lists

    >>> sum_nested([1, [2], [3, 4], [[5, 6], 7]])
    28
    >>> sum_nested([[1, [2]], [[[3]]], 4, [[5, 6], [[[7]]]]])
    28
    """
    count = 0
    if isinstance(obj, int):
        return obj
    for elem in obj:
        count += sum_nested(elem)
    return count

def flatten(obj: Union[int, list]) -> List[int]:
    """Return a (non-nested) list of the integers in <obj>.

    The integers are returned in the left-to-right order they appear
    in <obj>.

    >>> flatten(6)
    [6]
    >>> flatten([1, [-2, 3], -4])
    [1, -2, 3, -4]
    >>> flatten([[0, -1], -2, [[-3, [-5]]]])
    [0, -1, -2, -3, -5]
    """
    lst = []
    if isinstance(obj, int):
        return [obj]
    for elem in obj:
        if isinstance(elem, list):
            lst.extend(flatten(elem))
        else:
            lst.append(elem)
    return lst


def nested_list_contains(obj: Union[int, List], item: int) -> bool:
    """Return whether the given item appears in <obj>.

    >>> nested_list_contains(13, 13)
    True
    >>> nested_list_contains(13, 4)
    False
    >>> nested_list_contains([[1, 2, 3], 4, [[5]]], 5)
    True
    """

    if isinstance(obj, int):
        if obj == item:
            return True
    else:
        for elem in obj:
            if nested_list_contains(elem, item):
                return True
    return False

def semi_homogeneous(obj: Union[int, List]) -> bool:
    """Return whether the given nested list is semi-homogeneous.

    A single integer and empty list are semi-homogeneous.
    In general, a list is semi-homogeneous if and only if:
        - all of its sub-nested-lists are integers, or all of them are lists
        - all of its sub-nested-lists are semi-homogeneous

    >>> semi_homogeneous(10)
    True
    >>> semi_homogeneous([])
    True
    >>> semi_homogeneous([1, 2, 3])
    True
    >>> semi_homogeneous([1, [2], 3])
    False
    >>> semi_homogeneous([[1, 2], [[3, 4]], [[[5]]]])
    True
    >>> semi_homogeneous([[1, 2], [[3, 4]], [[[5]]], 9])
    False
    """

    pass




if __name__ == '__main__':
    import doctest
    doctest.testmod()
