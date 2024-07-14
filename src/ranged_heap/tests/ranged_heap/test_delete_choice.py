import pytest

import ranged_heap as rh


def test_delete_choice(ranged_heap: rh.RangedHeap):
    """Test deleting a choice from the RangedHeap.

    Args:
        ranged_heap (rh.RangedHeap): The RangedHeap instance from which the choice is deleted.

    Asserts:
        The size of the RangedHeap decreases by 1 and the deleted choice is no longer in its corresponding range.
    """
    size_before_remove = len(ranged_heap)
    ranged_heap.delete_choice("c2", 2)

    assert len(ranged_heap) == size_before_remove - 1
    assert "c2" not in ranged_heap.ranged[2]

def test_delete_choice_invalid_choice_error(ranged_heap: rh.RangedHeap):
    """Test deleting an invalid choice from the RangedHeap raises InvalidChoiceError.

    Args:
        ranged_heap (rh.RangedHeap): The RangedHeap instance from which the invalid choice deletion is attempted.

    Asserts:
        An InvalidChoiceError is raised when attempting to delete a choice with a value greater than the allowed maximum.
    """
    value = len(ranged_heap) + 1
    with pytest.raises(rh.InvalidChoiceError):
        ranged_heap.delete_choice(key="c2", value=value)

def test_delete_choice_choice_not_found_error(ranged_heap: rh.RangedHeap):
    """Test deleting a choice that does not exist in the RangedHeap raises ChoiceNotFoundError.

    Args:
        ranged_heap (rh.RangedHeap): The RangedHeap instance from which the non-existent choice deletion is attempted.

    Asserts:
        A ChoiceNotFoundError is raised when attempting to delete a choice that does not exist in the RangedHeap.
    """
    with pytest.raises(rh.ChoiceNotFoundError):
        ranged_heap.delete_choice(key="c2", value=1)
