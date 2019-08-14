from partition_alt import partition


def quicksort(a: list, l: int, u: int) -> None:
    """Sort the given list a in non-descending order.
    Precondition: 0 <= l and u < len(a)
  >>> a = [4,2,1,5,6]
  >>> l = 0
  >>> u = 4
  >>> quicksort(a,l,u)
  >>> print(a)
  [1, 2, 4, 5, 6]
  >>> a = [5,3,2,1,8]
  >>> l = 0
  >>> u = 4
  >>> quicksort(a,l,u)
  >>> print(a)
  [1, 2, 3, 5, 8]
  """

    if l < u:
        mid = (l + u) // 2
        three = [a[l], a[mid], a[u]]
        three.sort()
        if three[1] == a[l]:
            pivot_loc = l
        elif three[1] == a[u]:
            pivot_loc = u
        else:
            pivot_loc = mid
        a[u], a[pivot_loc] = a[pivot_loc], a[u]
        pivot = a[u]
        part = partition(a, l, u, pivot)
        i = part[0]
        j = part[1]
        a[i], a[u] = a[u], a[i]
        quicksort(a, j, u)
        quicksort(a, l, i)
"""
 ORiginal
  if l < u:
    mid = (l + u) // 2
    three = [a[l], a[mid], a[u]]
    three.sort()
    if three[1] == a[l]:
      pivot_loc = l
    elif three[1] == a[u]:
      pivot_loc = u
    else:
      pivot_loc = mid
    a[u], a[pivot_loc] = a[pivot_loc], a[u]
    pivot = a[u]
    i = partition(a, l, u - 1, pivot)
    a[i], a[u] = a[u], a[i]
    quicksort(a, l, i - 1)
    quicksort(a, i + 1, u)
"""

