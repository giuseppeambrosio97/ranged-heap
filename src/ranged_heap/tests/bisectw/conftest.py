import pytest


@pytest.fixture
def sorted_list():
    return sorted([1, 2, 3, 4, 5, 6, 7, 8, 9])
