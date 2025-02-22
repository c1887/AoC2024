def parse_input(file_name) -> list[list[int]]:
    out: list[list[int]] = []
    with open(file_name) as f:
        for line in f.readlines():
            numbers = [int(i) for i in line.split()]
            out.append(numbers)
    return out


def is_safe(line: list[int]) -> bool:
    if line[0] == line[1]:
        return False

    is_increasing = line[0] < line[1]
    input = line if is_increasing else list(reversed(line))
    last = input[0]
    for next in input[1:]:
        if next - last not in [1, 2, 3]:
            return False
        last = next
    return True


def is_safe_single_removal(line: list[int]) -> bool:
    """Brute force try, runs fast enough."""
    if is_safe(line):
        return True
    for skip_index in range(len(line)):
        if is_safe(line[:skip_index] + line[skip_index + 1 :]):
            return True
    return False


def part_1(lines: list[list[int]]) -> int:
    return sum(is_safe(line) for line in lines)


def part_2(lines: list[list[int]]) -> int:
    return sum(is_safe_single_removal(line) for line in lines)


if __name__ == "__main__":
    # print(parse_input("day2.txt"))
    input = parse_input("day2.txt")
    print(part_1(input))
    print(part_2(input))
