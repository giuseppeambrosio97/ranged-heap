from typing import List
from bisect import bisect_left, insort_left


def bs_delete(a: List[int], x: int) -> int:
    """
    Deletes the first occurrence of `x` from the sorted list `a`.

    Args:
        a (List[int]): Sorted list of int numbers.
        x (int): Element to be deleted from `a`.

    Returns:
        int: Index of the deleted element if found, otherwise -1.

    Time Complexity:
        O(log n + n), where n is the length of list `a`.
    """
    pos = bisect_left(a, x)  # O(log n)
    if pos < len(a) and a[pos] == x:
        del a[pos]  # O(n)
        return pos
    return -1


def bs_add(a: List[int], x: int) -> int:
    """
    Adds `x` to the sorted list `a` while maintaining sorted order.

    Args:
        a (List[int]): Sorted list of int numbers.
        x (int): Element to be added to `a`.

    Returns:
        int: Index where `x` was inserted.

    Time Complexity:
        O(log n + n), where n is the length of list `a`.
    """
    pos = bisect_left(a, x)  # O(log n)
    insort_left(a, x)  # O(n)
    return pos
