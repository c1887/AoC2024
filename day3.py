def parse_input(file_name) -> list[str]:
    out: list[str] = []
    with open(file_name) as f:
        out = [line for line in f.readlines()]
    return out



if __name__ == "__main__":
    # print(parse_input("day3.txt"))
    input = parse_input("day3.txt")
    # print(part_1(input))
    # print(part_2(input))
