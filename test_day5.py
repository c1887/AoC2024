from day5 import (
    Ordering,
    _create_order_dict,
    correct_order,
    is_correctly_ordered,
    part_1,
    part_2,
)


def test_create_order_dict() -> None:
    input = [[1, 2], [1, 3], [2, 4]]
    result = _create_order_dict(input)
    assert result[1] == [2, 3]
    assert result[2] == [4]


def test_ordering() -> None:
    ordering = Ordering([[1, 2], [1, 3]])
    assert ordering.correct_order(1, 2)
    assert ordering.correct_order(1, 3)
    assert not ordering.correct_order(3, 1)

    # some we have no information on, these are ok as well.
    assert ordering.correct_order(41, 42)
    assert ordering.correct_order(42, 41)


def test_correct_update() -> None:
    ordering = Ordering([[1, 2], [1, 3]])
    assert is_correctly_ordered(ordering, [1, 2, 3])
    assert is_correctly_ordered(ordering, [1, 3, 2, 4])
    assert not is_correctly_ordered(ordering, [3, 1, 2, 4])


def test_correct_order() -> None:
    ordering = Ordering([[1, 2], [1, 3]])
    faulty = [3, 1, 2, 4]
    assert not is_correctly_ordered(ordering, faulty)
    corrected = correct_order(ordering, faulty)
    assert is_correctly_ordered(ordering, corrected)
    # do we still have the same elements?
    assert sorted(faulty) == sorted(corrected)


def test_example() -> None:
    orderings = [
        [47, 53],
        [97, 13],
        [97, 61],
        [97, 47],
        [75, 29],
        [61, 13],
        [75, 53],
        [29, 13],
        [97, 29],
        [53, 29],
        [61, 53],
        [97, 53],
        [61, 29],
        [47, 13],
        [75, 47],
        [97, 75],
        [47, 61],
        [75, 61],
        [47, 29],
        [75, 13],
        [53, 13],
    ]
    updates = [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]
    assert part_1(orderings, updates) == 143
    assert part_2(orderings, updates) == 123
