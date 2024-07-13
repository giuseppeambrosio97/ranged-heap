import typing

import ranged_heap as rh


def test_bs_delete_existing_element(sorted_list: typing.List[int]):
    index_deleted = rh.bs_delete(sorted_list, 3)
    assert index_deleted == 2
    assert sorted_list == [1, 2, 4, 5, 6, 7, 8, 9]


def test_bs_delete_non_existing_element(sorted_list: typing.List[int]):
    index_deleted = rh.bs_delete(sorted_list, 10)
    assert index_deleted == -1
    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_bs_delete_last_element(sorted_list: typing.List[int]):
    index_deleted = rh.bs_delete(sorted_list, 9)
    assert index_deleted == 8
    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8]


def test_bs_delete_first_element(sorted_list: typing.List[int]):
    index_deleted = rh.bs_delete(sorted_list, 1)
    assert index_deleted == 0
    assert sorted_list == [2, 3, 4, 5, 6, 7, 8, 9]


def test_bs_delete_empty_list():
    empty_list = []
    index_deleted = rh.bs_delete(empty_list, 1)
    assert index_deleted == -1
