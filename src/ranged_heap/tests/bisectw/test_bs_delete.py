import typing

import ranged_heap as rh


def test_bs_delete_existing_element(sorted_list: typing.List[int]):
    """Test deleting an existing element from a sorted list using binary search.

    Args:
        sorted_list (typing.List[int]): The sorted list from which the element is deleted.

    Asserts:
        The index of the deleted element and the updated sorted list.
    """
    index_deleted = rh.bs_delete(sorted_list, 3)
    assert index_deleted == 2
    assert sorted_list == [1, 2, 4, 5, 6, 7, 8, 9]

def test_bs_delete_non_existing_element(sorted_list: typing.List[int]):
    """Test deleting a non-existing element from a sorted list using binary search.

    Args:
        sorted_list (typing.List[int]): The sorted list from which the element is attempted to be deleted.

    Asserts:
        The index of the deleted element and the updated sorted list.
    """
    index_deleted = rh.bs_delete(sorted_list, 10)
    assert index_deleted == -1
    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_bs_delete_last_element(sorted_list: typing.List[int]):
    """Test deleting the last element from a sorted list using binary search.

    Args:
        sorted_list (typing.List[int]): The sorted list from which the element is deleted.

    Asserts:
        The index of the deleted element and the updated sorted list.
    """
    index_deleted = rh.bs_delete(sorted_list, 9)
    assert index_deleted == 8
    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8]

def test_bs_delete_first_element(sorted_list: typing.List[int]):
    """Test deleting the first element from a sorted list using binary search.

    Args:
        sorted_list (typing.List[int]): The sorted list from which the element is deleted.

    Asserts:
        The index of the deleted element and the updated sorted list.
    """
    index_deleted = rh.bs_delete(sorted_list, 1)
    assert index_deleted == 0
    assert sorted_list == [2, 3, 4, 5, 6, 7, 8, 9]

def test_bs_delete_empty_list():
    """Test deleting an element from an empty list using binary search.

    Asserts:
        The index of the deleted element.
    """
    empty_list = []
    index_deleted = rh.bs_delete(empty_list, 1)
    assert index_deleted == -1
