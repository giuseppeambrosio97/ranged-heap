import pytest

import ranged_heap as rh


def test_add_choice(ranged_heap: rh.RangedHeap):
    size_before_add = len(ranged_heap)
    ranged_heap.add_choice("c7", 2)

    assert len(ranged_heap) == size_before_add + 1
    assert "c7" in ranged_heap.ranged[2]


def test_add_choice_invalid_choice_error(ranged_heap: rh.RangedHeap):
    value = len(ranged_heap) + 1
    with pytest.raises(rh.InvalidChoiceError):
        ranged_heap.add_choice(key="c10", value=value)
