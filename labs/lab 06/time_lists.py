from linked_list import LinkedList
from typing import Tuple
import time


def profile_len(list_size: int, n: int) -> Tuple[float, float]:
    """Return the average time taken (averaging over <n> repetitions) to
    call len on a Python list of length <list_size> and to call len on a
    LinkedList of length <list_size>.
    """
    # Make both a Python list and a LinkedList of size <list_size>.
    lst = list(range(list_size))
    ll = LinkedList(lst)

    start = time.time()
    for i in range(n):
        len(lst)
    end = time.time()
    time1 = end - start

    start = time.time()
    for i in range(n):
        len(ll)
    end = time.time()
    time2 = end - start

    return time1, time2


if __name__ == '__main__':
    sizes = [10000, 20000, 40000, 80000, 100000]

    # For each size of list, profile len for a Python list vs a LinkedList,
    # and print the results.
    for s in sizes:
        results = profile_len(s, 1000)
        print('Size = {}, avg time for len(lst): {:.8f} and for len(ll): {:.8f}'
              .format(s, results[0], results[1]))
