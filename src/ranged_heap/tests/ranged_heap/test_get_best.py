import pytest

import ranged_heap as rh


def test_get_best(ranged_heap: rh.RangedHeap):
    """Test retrieving the best choice from the RangedHeap.

    Args:
        ranged_heap (rh.RangedHeap): The RangedHeap instance from which the best choice is retrieved.

    Asserts:
        The best choice retrieved matches the expected result.
    """
    best_choice = ranged_heap.get_best()
    assert best_choice == "c5"

def test_get_best_empty(ranged_heap_empty: rh.RangedHeap):
    """Test retrieving the best choice from an empty RangedHeap raises EmptyHeapError.

    Args:
        ranged_heap_empty (rh.RangedHeap): The empty RangedHeap instance from which the retrieval is attempted.

    Asserts:
        An EmptyHeapError is raised when attempting to retrieve the best choice from an empty RangedHeap.
    """
    with pytest.raises(rh.EmptyHeapError):
        ranged_heap_empty.get_best()
