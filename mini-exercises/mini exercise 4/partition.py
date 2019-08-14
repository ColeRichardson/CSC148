from typing import List, Any


def partition(a: List, l: int, u: int, pivot: Any) -> int:
    """
    Rearrange list <a> so that elements greater than or equal to <pivot> follow
    all elements less than pivot. Return index of first element >= pivot.
    """

    i = l
    j = l
    while j <= u:
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1
    return i
