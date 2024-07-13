import pytest

import ranged_heap as rh

# from tests import RANGED_HEAP_STR_PATH

@pytest.fixture
def ranged_heap():
    """Provide a fixture that returns a RangedHeap instance with predefined choices.

    Returns:
        rh.RangedHeap: A RangedHeap instance with k=4 and a list of choices.
    """
    choices = [
        ("c1", 1),
        ("c2", 2),
        ("c3", 3),
        ("c4", 1),
        ("c5", 0),
        ("c6", 6),
    ]
    return rh.RangedHeap(k=6, choices=choices)

# def ranged_heap_str():
#     with open(RANGED_HEAP_STR_PATH) as f:
#         return f.read()

@pytest.fixture
def ranged_heap_empty():
    """Provide a fixture that returns an empty RangedHeap instance.

    Returns:
        rh.RangedHeap: A RangedHeap instance with k=4 and no choices.
    """
    return rh.RangedHeap(k=4, choices=[])

# print(ranged_heap_str)
