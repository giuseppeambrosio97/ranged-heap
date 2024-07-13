import typing

import ranged_heap as rh


def test_bs_add_existing_element(sorted_list: typing.List[int]):
    """Test adding an existing element to a sorted list using binary search.

    Args:
        sorted_list (typing.List[int]): The sorted list to which the element is added.

    Asserts:
        The index of the added element and the updated sorted list.
    """
    index_added = rh.bs_add(sorted_list, 3)
    assert index_added == 2
    assert sorted_list == [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]

def test_bs_add_greater_than_max(sorted_list: typing.List[int]):
    """Test adding an element greater than the maximum element in a sorted list.

    Args:
        sorted_list (typing.List[int]): The sorted list to which the element is added.

    Asserts:
        The index of the added element and the updated sorted list.
    """
    index_added = rh.bs_add(sorted_list, 10)
    assert index_added == 9
    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_bs_add_less_than_min(sorted_list: typing.List[int]):
    """Test adding an element less than the minimum element in a sorted list.

    Args:
        sorted_list (typing.List[int]): The sorted list to which the element is added.

    Asserts:
        The index of the added element and the updated sorted list.
    """
    index_added = rh.bs_add(sorted_list, 0)
    assert index_added == 0
    assert sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_bs_add_empty_list():
    """Test adding an element to an empty list.

    Asserts:
        The index of the added element and the updated list.
    """
    empty_list = []
    index_added = rh.bs_add(empty_list, 1)
    assert index_added == 0
    assert empty_list == [1]
