from utils import get_puzzle_input


def parse_data(data: list[str]) -> list[int]:
    splited_data = data[0].strip().split(',')
    return list(map(lambda position: int(position), splited_data))


def calculate_alignment_target_position(data: list[int]) -> tuple[int, int]:
    data_set = set(data)
    counter = {number: 0 for number in data}

    for fixed_position in data_set:
        count = 0
        for position in data:
            count += abs(fixed_position - position)
        counter[fixed_position] = count

    counter_values = counter.values()
    counter_keys = list(counter.keys())

    cheaper, *counter_values = counter_values

    for value in counter_values:
        if value < cheaper:
            cheaper = value

    target_index = counter_values.index(cheaper) + 1
    return (counter_keys[target_index], cheaper)


if __name__ == "__main__":
    # # test {{{
    # puzzle_input = ["16,1,2,0,4,2,7,1,2,14"]
    # data = parse_data(puzzle_input)
    # print(data)
    # target, fuel = calculate_alignment_target_position(data)
    # print(target, fuel)
    # # }}}

    # main {{{
    if puzzle_input := get_puzzle_input("day7.input"):
        clean_data = parse_data(puzzle_input)
        target, fuel = calculate_alignment_target_position(clean_data)
        print(target, fuel)
    # }}}
