import pytest

import ranged_heap as rh


def test_pop_best(ranged_heap: rh.RangedHeap):
    size_before_pop = len(ranged_heap)
    best_choice = ranged_heap.pop_best()

    assert best_choice == "c5"
    assert len(ranged_heap) == size_before_pop - 1


def test_pop_best_empty(ranged_heap_empty: rh.RangedHeap):
    with pytest.raises(rh.EmptyHeapError):
        _ = ranged_heap_empty.pop_best()
