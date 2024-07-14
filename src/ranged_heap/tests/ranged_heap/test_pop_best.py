import pytest

import ranged_heap as rh


def test_pop_best(ranged_heap: rh.RangedHeap):
    """Test popping the best choice from the RangedHeap.

    Args:
        ranged_heap (rh.RangedHeap): The RangedHeap instance from which the best choice is popped.

    Asserts:
        The popped best choice matches the expected result, and the length of the RangedHeap decreases by 1.
    """
    size_before_pop = len(ranged_heap)
    best_choice = ranged_heap.pop_best()

    assert best_choice == "c5"
    assert len(ranged_heap) == size_before_pop - 1

def test_pop_best_empty(ranged_heap_empty: rh.RangedHeap):
    """Test popping the best choice from an empty RangedHeap raises EmptyHeapError.

    Args:
        ranged_heap_empty (rh.RangedHeap): The empty RangedHeap instance from which the pop operation is attempted.

    Asserts:
        An EmptyHeapError is raised when attempting to pop the best choice from an empty RangedHeap.
    """
    with pytest.raises(rh.EmptyHeapError):
        ranged_heap_empty.pop_best()
