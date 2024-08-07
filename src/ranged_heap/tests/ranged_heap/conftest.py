import pytest

import ranged_heap as rh
from tests import RANGED_HEAP_STR_PATH


@pytest.fixture
def ranged_heap() -> rh.RangedHeap:
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

@pytest.fixture
def ranged_heap_str() -> str:
    """Provide a fixture that reads the contents of a file located at RANGED_HEAP_STR_PATH and returns it as a string.

    This fixture is useful for tests that require access to the file's content without explicitly opening the file within each test. It abstracts the file reading operation, making tests cleaner and focusing on the logic rather than file handling.

    Returns:
    - str: The content of the file located at RANGED_HEAP_STR_PATH.
    """
    with open(RANGED_HEAP_STR_PATH) as f:
        return f.read()

@pytest.fixture
def ranged_heap_empty() -> rh.RangedHeap:
    """Provide a fixture that returns an empty RangedHeap instance.

    Returns:
        rh.RangedHeap: A RangedHeap instance with k=4 and no choices.
    """
    return rh.RangedHeap(k=4, choices=[])

