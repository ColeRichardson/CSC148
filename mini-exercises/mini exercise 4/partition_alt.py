from typing import List, Any, Tuple


def partition(a: List, l: int, u: int, pivot: Any) -> Tuple[int, int]:
    """
    Alternate partition: This new partition procedure maintains two
    split points, dividing the list into those elements that are smaller
    than the pivot, those exactly equal to the pivot, and those strictly
    larger than the pivot. Return a tuple of the indices of the two split points.

    >>> l = [-19, 1, 1, 1, 18, 18, 104, 418]
    >>> partition(l, 0, len(l)-1, 18)
    (4, 6)
    >>> l
    [-19, 1, 1, 1, 18, 18, 418, 104]
    """

    i = l
    j = l
    k = u
    while j <= k:
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        elif a[j] == pivot:
            j += 1
        else:
            a[j], a[k] = a[k], a[j]
            k -= 1
    return (i, j)
