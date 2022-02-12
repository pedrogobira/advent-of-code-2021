from utils import get_puzzle_input


def parse_data(data: list[str]) -> list[int]:
    data = list(*map(lambda numbers: numbers.split(","), data))
    clean_data = list(map(int, data))

    return clean_data


def calculate_growth(data: list[int], limit: int = 80) -> int:
    help_list = []

    while limit != 0:
        for number in data:
            if number > 0:
                help_list.append(number - 1)
            elif number == 0:
                help_list.append(number + 6)
                help_list.insert(data[-1], 8)
        data = help_list
        help_list = []
        limit -= 1

    return len(data)


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
        result = calculate_growth(clean_data)
        print(result)
    # }}}
