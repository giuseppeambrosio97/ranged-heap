import pytest

import ranged_heap as rh


def test_ranged_heap_len(ranged_heap: rh.RangedHeap):
    assert len(ranged_heap) == 6


def test_ranged_heap_negative_k():
    with pytest.raises(rh.InvalidRangeError):
        _ = rh.RangedHeap(k=-1, choices=None)
