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
    """Takes a list of strings like mul(xx,yy) and returns [xx*yy, ...]."""
    p = re.compile("mul\(\d{1,3},\d{1,3}\)")
    prod_strs = p.findall(word)

    return [str_to_int_prod(w) for w in prod_strs]


def do_dont_products(word: str) -> list[str]:
    p = re.compile("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
    return p.findall(word)


class EnableDisableMachine:
    """Stateful callable which is either enabled or disabled.

    If we found a don't(), we are disabled until the next do().
    For anything which is not mul(...), we always return False, but may
    change the state of the machine.

    For a string like mul(...), we return True or False depending on the state
    of the machine (i.e. if it is enabled or not).
    """

    def __init__(self):
        self.enabled = True

    def __call__(self, word: str) -> bool:
        if word == "don't()":
            self.enabled = False
            return False
        elif word == "do()":
            self.enabled = True
            return False
        return self.enabled


def filter_donts(words: list[str]) -> list[str]:
    enabled = EnableDisableMachine()
    return [word for word in words if enabled(word)]


def part_1(words: list[str]) -> int:
    return sum([sum(products(word)) for word in words])

def list_to_single_str(words: list[str]) -> str:
    return "".join(words)

def part_2(words: list[str]) -> int:
    # Maybe, the lines are not to be looked at individually, but the disabled state works
    # across lines?
    big_word = list_to_single_str(words)
    filtered_words = filter_donts(do_dont_products(big_word))
    return sum(products(list_to_single_str(filtered_words)))


if __name__ == "__main__":
    # print(parse_input("day3.txt"))
    input = parse_input("day3.txt")
    print(part_1(input))
    print(part_2(input))
