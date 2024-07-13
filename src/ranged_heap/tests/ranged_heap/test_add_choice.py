import pytest

import ranged_heap as rh


def test_add_choice(ranged_heap: rh.RangedHeap):
    """Test adding a valid choice to the RangedHeap.

    Args:
        ranged_heap (rh.RangedHeap): The RangedHeap instance to which the choice is added.

    Asserts:
        The size of the RangedHeap after adding the choice and the presence of the new choice.
    """
    size_before_add = len(ranged_heap)
    new_choice_value = 5
    ranged_heap.add_choice("c7", new_choice_value)

    assert len(ranged_heap) == size_before_add + 1
    assert "c7" in ranged_heap.ranged[new_choice_value]

def test_add_choice_invalid_choice_error(ranged_heap: rh.RangedHeap):
    """Test adding an invalid choice to the RangedHeap raises an InvalidChoiceError.

    Args:
        ranged_heap (rh.RangedHeap): The RangedHeap instance to which the invalid choice is attempted to be added.

    Asserts:
        An InvalidChoiceError is raised when adding a choice with a value greater than the length of the RangedHeap.
    """
    value = len(ranged_heap) + 1
    with pytest.raises(rh.InvalidChoiceError):
        ranged_heap.add_choice(key="c10", value=value)
