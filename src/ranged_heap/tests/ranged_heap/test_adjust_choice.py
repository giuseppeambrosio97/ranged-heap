import pytest

import ranged_heap as rh


def test_adjust_choice(ranged_heap: rh.RangedHeap):
    """Test adjusting a choice in the RangedHeap.

    Args:
        ranged_heap (rh.RangedHeap): The RangedHeap instance in which the choice is adjusted.

    Asserts:
        The size of the RangedHeap remains unchanged, the old value is removed from its previous range,
        and the new value is added to the appropriate range.
    """
    size_before_adjust = len(ranged_heap)
    ranged_heap.adjust_choice("c4", 1, 3)

    assert len(ranged_heap) == size_before_adjust
    assert "c4" not in ranged_heap.ranged[1]
    assert "c4" in ranged_heap.ranged[3]

def test_adjust_choice_old_value_invalid_choice_error(ranged_heap: rh.RangedHeap):
    """Test adjusting a choice in the RangedHeap with an invalid old value raises InvalidChoiceError.

    Args:
        ranged_heap (rh.RangedHeap): The RangedHeap instance in which the invalid adjustment is attempted.

    Asserts:
        An InvalidChoiceError is raised when the old value is greater than the allowed maximum.
    """
    value = ranged_heap.k + 1
    with pytest.raises(rh.InvalidChoiceError):
        ranged_heap.adjust_choice(key="c10", old_value=value + 1, new_value=0)

def test_adjust_choice_new_value_invalid_choice_error(ranged_heap: rh.RangedHeap):
    """Test adjusting a choice in the RangedHeap with an invalid new value raises InvalidChoiceError.

    Args:
        ranged_heap (rh.RangedHeap): The RangedHeap instance in which the invalid adjustment is attempted.

    Asserts:
        An InvalidChoiceError is raised when the new value is greater than the allowed maximum.
    """
    value = len(ranged_heap) + 1
    with pytest.raises(rh.InvalidChoiceError):
        ranged_heap.adjust_choice(key="c10", old_value=0, new_value=value + 1)

def test_adjust_choice_choice_not_found_error(ranged_heap: rh.RangedHeap):
    """Test adjusting a choice in the RangedHeap that does not exist raises ChoiceNotFoundError.

    Args:
        ranged_heap (rh.RangedHeap): The RangedHeap instance in which the adjustment is attempted.

    Asserts:
        A ChoiceNotFoundError is raised when attempting to adjust a choice that does not exist in the RangedHeap.
    """
    with pytest.raises(rh.ChoiceNotFoundError):
        ranged_heap.adjust_choice(key="c10", old_value=1, new_value=1)
