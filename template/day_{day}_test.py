import pytest
from common.utils import read_file
from day_{day} import p1, p2


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "\{day\}/test_input.txt", 0, id="test_input.txt",
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
            "\{day\}/test_input.txt", 0, id="test - 1",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected
