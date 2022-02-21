from utils import get_puzzle_input


def parse_data(data: list[str]) -> list[list[str]]:
    return list(
        map(lambda position: position.strip().split("|")[1].strip().split(" "), data)
    )


def count_unique_segment_numbers(data: list[list[str]]) -> int:
    count = 0

    for digits in data:
        for number in digits:
            if len(number) in [2, 3, 4, 7]:
                count += 1

    return count


if __name__ == "__main__":
    # main {{{
    if puzzle_input := get_puzzle_input("day8.input"):
        clean_data = parse_data(puzzle_input)
        count_result = count_unique_segment_numbers(clean_data)
        print(count_result)
    # }}}
