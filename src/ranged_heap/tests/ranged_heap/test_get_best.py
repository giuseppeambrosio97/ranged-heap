import pytest

import ranged_heap as rh


def test_get_best(ranged_heap: rh.RangedHeap):
    best_choice = ranged_heap.get_best()
    assert best_choice == "c5"


def test_get_best_empty(ranged_heap_empty: rh.RangedHeap):
    with pytest.raises(rh.EmptyHeapError):
        _ = ranged_heap_empty.get_best()
