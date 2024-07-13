import pytest

import ranged_heap as rh


def test_ranged_heap_len(ranged_heap: rh.RangedHeap):
    """Test the length of the RangedHeap.

    Args:
        ranged_heap (rh.RangedHeap): The RangedHeap instance whose length is tested.

    Asserts:
        The length of the RangedHeap matches the expected value.
    """
    assert len(ranged_heap) == 6

def test_ranged_heap_negative_k():
    """Test creating a RangedHeap with a negative k value raises InvalidRangeError.

    Asserts:
        An InvalidRangeError is raised when attempting to create a RangedHeap with k=-1.
    """
    with pytest.raises(rh.InvalidRangeError):
        rh.RangedHeap(k=-1, choices=None)
