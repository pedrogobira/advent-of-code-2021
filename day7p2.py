from utils import get_puzzle_input
from statistics import mean


def parse_data(data: list[str]) -> list[int]:
    return [int(position) for position in data[0].strip().split(",")]


def calculate_alignment(data: list[int]) -> tuple[int, int]:
    mean_position = int(mean(data))
    count = 0

    for position in data:
        count += sum(range(abs(mean_position - position) + 1))

    return (mean_position, count)


if __name__ == "__main__":
    # # test {{{
    # puzzle_input = ["16,1,2,0,4,2,7,1,2,14"]
    # data = parse_data(puzzle_input)
    # target, fuel = calculate_alignment_target_position(data)
    # print(target, fuel)
    # # }}}

    # main {{{
    if puzzle_input := get_puzzle_input("day7.input"):
        clean_data = parse_data(puzzle_input)
        target, fuel = calculate_alignment(clean_data)
        print(f"Target position for alignment: {target}; Fuel consumption: {fuel}")
    # }}}
