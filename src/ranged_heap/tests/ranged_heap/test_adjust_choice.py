import pytest

import ranged_heap as rh


def test_adjust_choice(ranged_heap: rh.RangedHeap):
    size_before_adjust = len(ranged_heap)
    ranged_heap.adjust_choice("c4", 1, 3)

    assert len(ranged_heap) == size_before_adjust
    assert "c4" not in ranged_heap.ranged[1]
    assert "c4" in ranged_heap.ranged[3]


def test_adjust_choice_old_value_invalid_choice_error(ranged_heap: rh.RangedHeap):
    value = ranged_heap.k + 1
    with pytest.raises(rh.InvalidChoiceError):
        ranged_heap.adjust_choice(key="c10", old_value=value + 1, new_value=0)


def test_adjust_choice_new_value_invalid_choice_error(ranged_heap: rh.RangedHeap):
    value = len(ranged_heap) + 1
    with pytest.raises(rh.InvalidChoiceError):
        ranged_heap.adjust_choice(key="c10", old_value=0, new_value=value + 1)


def test_adjust_choice_choice_not_found_error(ranged_heap: rh.RangedHeap):
    with pytest.raises(rh.ChoiceNotFoundError):
        ranged_heap.adjust_choice(key="c10", old_value=1, new_value=1)
