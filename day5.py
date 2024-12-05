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


def is_correctly_ordered(ordering: Ordering, update: list[int]) -> bool:
    return all(ordering.correct_order(a, b) for a, b in zip(update, update[1:]))


def part_1(orderings: list[list[int]], updates: list[list[int]]) -> int:
    ordering = Ordering(orderings)
    return sum(
        [
            get_middle_number(update)
            for update in updates
            if is_correctly_ordered(ordering, update)
        ]
    )


if __name__ == "__main__":
    # print(parse_input("day5.txt"))
    orders, updates = parse_input("day5.txt")
    print(part_1(orders, updates))
    # print(part_2(input))
