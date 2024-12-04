import pytest
from day4 import (
    count_xmas,
    right,
    left,
    up,
    down,
    up_left,
    up_right,
    down_left,
    down_right,
)


@pytest.fixture
def example() -> list[str]:
    return [
        "MMMSXXMASM",  #  0
        "MSAMXMSMSA",  # 1
        "AMXSXMAAMM",  # 2
        "MSAMASMSMX",  # 3
        "XMASAMXAMM",  # 4
        "XXAMMXXAMA",
        "SMSMSASXSS",  # 6
        "SAXAMASAAA",
        "MAMMMXMMMM",  # 8
        "MXMXAXMASX",
    ]


def test_right(example: list[str]) -> None:
    assert right(example, 4, 0)
    assert right(example, 0, 5)
    assert not right(example, 0, 4)
    assert not right(example, 3, 9)


def test_left(example: list[str]) -> None:
    assert left(example, 1, 4)
    assert not left(example, 0, 5)
    # Not an X:
    with pytest.raises(AssertionError):
        assert not left(example, 1, 0)


def test_up(example: list[str]) -> None:
    assert up(example, 5, 6)
    assert not up(example, 5, 0)
    # Not an X:
    with pytest.raises(AssertionError):
        assert not up(example, 1, 0)


def test_down(example: list[str]) -> None:
    assert down(example, 0, 1)
    assert not down(example, 0, 0)
    assert not down(example, 0, 3)
    assert not down(example, 3, 3)
    # Not an X:
    with pytest.raises(AssertionError):
        assert not down(example, 1, 1)


def test_up_left(example: list[str]) -> None:
    assert up_left(example, 5, 6)
    assert not up_left(example, 4, 6)


def test_up_right(example: list[str]) -> None:
    assert up_right(example, 9, 1)


def test_down_right(example: list[str]) -> None:
    assert down_right(example, 0, 4)
    assert not down_right(example, 5, 6)


def test_down_left(example: list[str]) -> None:
    assert down_left(example, 3, 9)


def test_example(example: list[str]) -> None:
    assert count_xmas(example) == 18
