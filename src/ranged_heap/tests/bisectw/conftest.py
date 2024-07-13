import pytest


@pytest.fixture
def sorted_list():
    """Provide a fixture that returns a sorted list of integers.

    Returns:
        list: A sorted list of integers from 1 to 9.
    """
    return sorted([1, 2, 3, 4, 5, 6, 7, 8, 9])
