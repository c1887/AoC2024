def parse_input(file_name) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []
    with open(file_name) as f:
        for line in f.readlines():
            numbers = line.split()
            assert len(numbers) == 2
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))
    return (left, right)

def generate_counts(right: list[int]) -> dict[int, int]:
    d: dict[int, int] = {}
    for n in right:
        d[n] = d.get(n, 0) + 1
    return d


def sim_score(left: list[int], count: dict[int]) -> int:
    products = [left_value * count.get(left_value, 0) for left_value in left]
    return sum(products)

def part_1(left: list[int], right: list[int]) -> int:
    ls = sorted(left)
    rs = sorted(right)
    diffs = [abs(l -r) for l, r in zip(ls, rs)]
    return sum(diffs)

def part_2(left: list[int], right: list[int]) -> int:
    return sim_score(left, generate_counts(right))


if __name__ == "__main__":
    left, right = parse_input("day1.txt")
    print(part_1(left, right))
    print(part_2(left, right))