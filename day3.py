import re


def parse_input(file_name) -> list[str]:
    out: list[str] = []
    with open(file_name) as f:
        out = [line for line in f.readlines()]
    return out


def str_to_int_prod(m: str) -> int:
    """Compute the actual product of mul(xx, yyy)"""
    m = m[4:-1]  # remove mul( )
    mm = m.split(",")
    assert len(mm) == 2
    return int(mm[0]) * int(mm[1])


def products(word: str) -> list[int]:
    p = re.compile("mul\(\d{1,3},\d{1,3}\)")
    prod_strs = p.findall(word)

    return [str_to_int_prod(w) for w in prod_strs]


def do_dont_products(word: str) -> list[str]:
    p = re.compile("mul\(\d{1,3},\d{1,3}\)|do\(\)|dont\(\)")
    return p.findall(word)


def filter_donts(words: list[str]) -> list[str]:
    pass


def part_1(words: list[str]) -> int:
    return sum([sum(products(word)) for word in words])


if __name__ == "__main__":
    # print(parse_input("day3.txt"))
    input = parse_input("day3.txt")
    print(part_1(input))
    # print(part_2(input))
