import pytest

import ranged_heap as rh


def test_delete_choice(ranged_heap: rh.RangedHeap):
    size_before_remove = len(ranged_heap)
    ranged_heap.delete_choice("c2", 2)

    assert len(ranged_heap) == size_before_remove - 1
    assert "c2" not in ranged_heap.ranged[2]


def test_delete_choice_invalid_choice_error(ranged_heap: rh.RangedHeap):
    value = len(ranged_heap) + 1
    with pytest.raises(rh.InvalidChoiceError):
        ranged_heap.delete_choice(key="c2", value=value)


def test_delete_choice_choice_not_found_error(ranged_heap: rh.RangedHeap):
    with pytest.raises(rh.ChoiceNotFoundError):
        ranged_heap.delete_choice(key="c2", value=1)
