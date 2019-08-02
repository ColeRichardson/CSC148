def rec_max(lst):
    '''(list of int, can be nested) -> int
    Return max number in possibly nested list of numbers.

    >>> rec_max([17, 21, 0])
    21
    >>> rec_max([17, [21, 24], 0])
    24

    Precondition: lst is not empty
    '''
    nums = []
    for element in lst:
        if isinstance(element, int):
            nums.append(element)
        else:
            nums.append(rec_max(element))
    return max(nums)


def rec_max2(lst):
    '''(list of int) -> int
    Return max number in possibly nested list of numbers.

    >>> rec_max2([17, 21, 0])
    21
    >>> rec_max2([17, [21, 24], 0])
    24

    '''
    if lst == []:
        return float('-inf')

    if isinstance(lst[0], int):
        return max(lst[0], rec_max2(lst[1:]))

    else:
        return max(rec_max2(lst[0]), rec_max2(lst[1:]))


# Variation of recursively finding max in nested list
def nested_max(obj: Union[int, List]) -> int:
    """Return the maximum integer stored in nested list <obj>.

    Return 0 if <obj> does not contain any integers.

    Precondition: all integers in <obj> are positive.

    >>> nested_max(17)
    17
    >>> nested_max([1, 2, [1, 2, [3], 4, 5], 4])
    5
    """

    best_so_far = 0
    for sublist in obj:
        if isinstance(elm, int):
            return elm
        best_so_far = max(best_so_far, nested_max(sublist))
    return best_so_far


import doctest

doctest.testmod()

import random

'''
Follow this recipe --
for elm in lst:
  if isinstance(elm, int):
    # ... base case
  else:
    # ... recursive call
'''

def sumlist(lst: list) -> int:
  """
  Return the sum of <lst>, which is arbitrarily nested.

  >>> sumlist([1, 2, [3, [4]], 5])
  15
  """

  s = 0
  for elm in lst:
    if isinstance(elm, int):
      s += elm # same as s = s + elm
    else:
      s += sumlist(elm)
  return s

def sumlist_odd(lst: list) -> int:
  """
  Return the sum of all odd elements in <lst>, which is arbitrarily nested.

  >>> sumlist_odd([1, 2, [3, [4]], 5])
  9
  """

  s = 0
  for elm in lst:
    if isinstance(elm, int):
      if elm % 2 == 1: # OR elm % 2 != 0
        s += elm
    else:
      s += sumlist_odd(elm)
  return s

def count_odd(lst: list) -> int:
  """
  Return the number of odd elements in the given arbitarily nested <lst>.
  """

  c = 0
  for elm in lst:
    if isinstance(elm, int):
      if elm % 2 == 1:
        c += 1
    else:
      c += count_odd(elm)
  return c

def get_odd(lst: list) -> list:
  """
  Return all the odd elements in the given arbitrarily nested <lst>.
  """

  new_lst = []
  for elm in lst:
    if isinstance(elm, int):
      if elm % 2 == 1:
        new_lst.append(elm)
    else:
      new_lst.extend(get_odd(elm))
  return c

# Try to complete the function below using what we already have above as
# helper functions. Try to do it in only one line.
def contains_odd(lst: list, num: int) -> bool:
  """
  Given lst nested to arbitrary depth, return true iff the list contains
  at least num amount of odd numbers.
  """

  pass


from __future__ import annotations


def remove_three(lst: list) -> List[int]:
    """
    Return a new list that removed all the threes from the given arbitrarily nested <lst>

    >>> lst = [1, 2, [3, 4, [1, 3]], 3]
    >>> remove_three(lst)
    [1, 2, [4, [1]]]
    """
    new_lst = []  # new list with no 3s
    for element in lst:
        if isinstance(element, int):
            if element != 3:
                new_lst.append(element)
        else:
            new_lst.append(remove_three(element))
    return new_lst


# A version of the above without using loop:
def remove_three2(lst: list) -> List[int]:
    """
    Return a new list that removed all the threes from the
    given arbitrarily nested <lst>

    >>> lst = [1, 2, [3, 4, [1, 3]], 3]
    >>> remove_three2(lst)
    [1, 2, [4, [1]]]
    """

    if len(lst) == 0:
        return []

    if isinstance(lst[0], int):
        if lst[0] == 3:  # if it is 3
            return remove_three2(lst[1:])
        else:  # if it is not 3
            return [lst[0]] + remove_three2(lst[1:])
    else:
        return [remove_three2(lst[0])] + remove_three2(lst[1:])


def add_one(lst: list) -> None:
    """
    Mutate the given arbitrarily nested <lst> by adding
    1 to every integer in the list.
    """

    # Hint: Think about indices
    # e.g. lst[0] = lst[0] + 1, this would mutate the list, but
    #      something like lst = new_lst does NOT change the original lst
    # Also: Remember that you are returning None

    # Solution below:
    for i in range(len(lst)):
        if isinstance(lst[i], int):
            lst[i] += 1
        else:
            add_one(lst[i])


import doctest

doctest.testmod()


