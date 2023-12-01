import pytest
from common.utils import read_file
from day_01 import p1, p2


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "01/test_input.txt", 142, id="test_input.txt",
        ),
    ],
)
def test_p1(filename, expected):
    # Test cases for p1 function
    assert p1(read_file(filename)) == expected


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "01/test_input_2.txt", 281, id="test - 1",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected
