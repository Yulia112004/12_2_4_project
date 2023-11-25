import pytest
from utils import arrs


ARRAY = [1, 2, 3]
@pytest.fixture
def coll():
    return ARRAY


def test_get(coll):
    assert arrs.get(coll, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(coll, 0) == 1


def test_slice(coll):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(coll, 1) == [2, 3]
    assert arrs.my_slice(coll, None, 2) == [1, 2]
    assert arrs.my_slice(coll, 2, None) == [3]
    assert arrs.my_slice([]) == []

