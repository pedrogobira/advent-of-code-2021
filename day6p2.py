from functools import reduce
from utils import get_puzzle_input


def parse_data(data: list[str]) -> list[int]:
    data = list(*map(lambda numbers: numbers.split(","), data))
    clean_data = list(map(int, data))

    return clean_data


def calculate_growth(data: list[int], limit: int = 80) -> int:
    counter = {x: 0 for x in range(10)}

    for number in data:
        counter[number] += 1

    while limit != 0:
        for number, count in counter.items():
            if number == 0:
                counter[0] = 0
                counter[9] += count
            elif number == 9:
                counter[6] += count
                counter[8] += count
                counter[9] = 0
            else:
                counter[number - 1] += count
                counter[number] = 0

        limit -= 1

    result = reduce(lambda x, y: x + y, counter.values())

    return result


if __name__ == "__main__":
    # # test {{{
    # puzzle_input = ["3,4,3,1,2"]
    # data = parse_data(puzzle_input)
    # result = calculate_growth(data)
    # print(result)
    # # }}}

    # main {{{
    if puzzle_input := get_puzzle_input("day6.input"):
        clean_data = parse_data(puzzle_input)
        result = calculate_growth(clean_data, limit=256)
        print(result)
    # }}}
