import pytest
from day4 import count_xmas, right, left, up, down


def test_right() -> None:
    example = ["XXXXX", "XXMAS"]
    assert right(example, 1, 1)
    assert not right(example, 0, 0)
    assert not right(example, 0, 3)
    assert not right(example, 1, 0)


def test_left() -> None:
    example = ["XXXXX", "SAMXX"]
    assert left(example, 1, 3)
    assert not left(example, 0, 0)
    assert not left(example, 0, 3)
    # Not an X:
    with pytest.raises(AssertionError):
        assert not left(example, 1, 0)


def test_up() -> None:
    example = ["XSXXX", "SAMXX", "XMXXA", "XXXXX"]
    assert up(example, 3, 1)
    assert not up(example, 0, 0)
    assert not up(example, 0, 3)
    assert not up(example, 3, 3)
    # Not an X:
    with pytest.raises(AssertionError):
        assert not up(example, 1, 0)


def test_down() -> None:
    example = ["XXXXX", "XMXXA", "SAMXX", "XSXXX"]
    assert down(example, 0, 1)
    assert not down(example, 0, 0)
    assert not down(example, 0, 3)
    assert not down(example, 3, 3)
    # Not an X:
    with pytest.raises(AssertionError):
        assert not down(example, 1, 1)


def test_example() -> None:
    example: list[str] = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMAS",
    ]
    assert count_xmas(example) == 18
