from functools import cmp_to_key


def parse_input(file_name) -> tuple[list[list[int]], list[list[int]]]:
    orders: list[list[int]] = []
    updates: list[list[int]] = []
    parsing_orders = True
    with open(file_name) as f:
        for line in f.readlines():
            if line.strip() == "":
                parsing_orders = False
                continue

            if parsing_orders:
                orders.append([int(i) for i in line.strip().split("|")])
            else:
                updates.append([int(i) for i in line.strip().split(",")])
    return (orders, updates)


def get_middle_number(update_list: list[int]) -> int:
    return update_list[len(update_list) // 2]


def _create_order_dict(orders: list[list[int]]) -> dict[int, list[int]]:
    collection: dict[int, list[int]] = {}
    for order in orders:
        collection[order[0]] = collection.get(order[0], list())
        collection[order[0]].append(order[1])
    return collection


class Ordering:
    def __init__(self, orders: list[list[int]]):
        self.order = _create_order_dict(orders)

    def correct_order(self, a: int, b: int) -> bool:
        return a not in self.order.get(b, [])

    def relative_compare(self, a: int, b: int) -> int:
        if b in self.order.get(a, []):
            return -1
        elif a in self.order.get(b, []):
            return 1
        return 0


def is_correctly_ordered(ordering: Ordering, update: list[int]) -> bool:
    return all(ordering.correct_order(a, b) for a, b in zip(update, update[1:]))


def correct_order(ordering: Ordering, update: list[int]) -> list[int]:
    return sorted(update, key=cmp_to_key(lambda a, b: ordering.relative_compare(a, b)))


def part_1(orderings: list[list[int]], updates: list[list[int]]) -> int:
    ordering = Ordering(orderings)
    return sum(
        [
            get_middle_number(update)
            for update in updates
            if is_correctly_ordered(ordering, update)
        ]
    )


def part_2(orderings: list[list[int]], updates: list[list[int]]) -> int:
    ordering = Ordering(orderings)
    corrected = [
        correct_order(ordering, update)
        for update in updates
        if not is_correctly_ordered(ordering, update)
    ]
    return sum([get_middle_number(update) for update in corrected])


if __name__ == "__main__":
    # print(parse_input("day5.txt"))
    orders, updates = parse_input("day5.txt")
    print(part_1(orders, updates))
    print(part_2(orders, updates))
