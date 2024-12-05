from day3 import list_to_single_str


def parse_input(file_name) -> list[list[int]]:
    with open(file_name) as f:
        return [line for line in f.readlines()]


def right(grid: list[str], row: int, col: int) -> bool:
    assert grid[row][col] == "X"

    if len(grid[row]) - 1 - col < 3:
        return False
    return grid[row][col + 1 : col + 4] == "MAS"


def left(grid: list[str], row: int, col: int) -> bool:
    assert grid[row][col] == "X"

    if col < 3:
        return False
    return grid[row][col - 3 : col] == "SAM"


def up(grid: list[str], row: int, col: int) -> bool:
    assert grid[row][col] == "X"

    if row < 3:
        return False
    word = list_to_single_str([grid[i][col] for i in range(row - 3, row)])
    return word == "SAM"


def down(grid: list[str], row: int, col: int) -> bool:
    assert grid[row][col] == "X"

    if len(grid) - 1 - row < 3:
        return False
    word = list_to_single_str([grid[i][col] for i in range(row + 1, row + 4)])
    return word == "MAS"


def up_left(grid: list[str], row: int, col: int) -> bool:
    assert grid[row][col] == "X"

    if row < 3 or col < 3:
        return False
    word = list_to_single_str(
        [grid[i][j] for i, j in zip(range(row - 3, row), range(col - 3, col))]
    )
    return word == "SAM"


def up_right(grid: list[str], row: int, col: int) -> bool:
    assert grid[row][col] == "X"

    if row < 3 or len(grid[row]) - 1 - col < 3:
        return False
    word = list_to_single_str(
        [
            grid[i][j]
            for i, j in zip(range(row - 3, row), reversed(range(col + 1, col + 4)))
        ]
    )
    return word == "SAM"


def down_right(grid: list[str], row: int, col: int) -> bool:
    assert grid[row][col] == "X"

    if len(grid) - 1 - row < 3 or len(grid[row]) - 1 - col < 3:
        return False
    word = list_to_single_str(
        [grid[i][j] for i, j in zip(range(row + 1, row + 4), range(col + 1, col + 4))]
    )
    return word == "MAS"


def down_left(grid: list[str], row: int, col: int) -> bool:
    assert grid[row][col] == "X"

    if len(grid) - 1 - row < 3 or col < 3:
        return False
    word = list_to_single_str(
        [
            grid[i][j]
            for i, j in zip(range(row + 1, row + 4), reversed(range(col - 3, col)))
        ]
    )
    return word == "MAS"


def is_star(grid: list[str], row: int, col: int) -> bool:
    assert grid[row][col] == "A"

    if len(grid) - 1 - row < 1 or col < 1 or row < 1 or len(grid[row]) - 1 - col < 1:
        return False
    # Check upper left:
    ul = grid[row - 1][col - 1]
    if ul == "M":
        return (
            grid[row - 1][col + 1] == "M"
            and grid[row + 1][col - 1] == "S"
            and grid[row + 1][col + 1] == "S"
            or grid[row - 1][col + 1] == "S"
            and grid[row + 1][col - 1] == "M"
            and grid[row + 1][col + 1] == "S"
        )
    elif ul == "S":
        return (
            grid[row - 1][col + 1] == "S"
            and grid[row + 1][col - 1] == "M"
            and grid[row + 1][col + 1] == "M"
            or grid[row - 1][col + 1] == "M"
            and grid[row + 1][col - 1] == "S"
            and grid[row + 1][col + 1] == "M"
        )
    # Faulty char
    return False


def count_xmas(grid: list[str]) -> int:
    # Strategy: find an 'X' and work from there in each
    # direction.
    ret = 0
    for rowidx in range(len(grid)):
        for colidx in range(len(grid[rowidx])):
            if grid[rowidx][colidx] == "X":
                ret += sum(
                    [
                        up(grid, rowidx, colidx),
                        down(grid, rowidx, colidx),
                        left(grid, rowidx, colidx),
                        right(grid, rowidx, colidx),
                        up_right(grid, rowidx, colidx),
                        up_left(grid, rowidx, colidx),
                        down_left(grid, rowidx, colidx),
                        down_right(grid, rowidx, colidx),
                    ]
                )
    return ret


def count_stars(grid: list[str]) -> int:
    # Strategy: find an 'A' and work from there in each
    # direction.
    ret = 0
    for rowidx in range(len(grid)):
        for colidx in range(len(grid[rowidx])):
            if grid[rowidx][colidx] == "A":
                ret += is_star(grid, rowidx, colidx)
    return ret


if __name__ == "__main__":
    # print(parse_input("day4.txt"))
    input = parse_input("day4.txt")
    print(count_xmas(input))
    print(count_stars(input))
    # print(part_2(input))
