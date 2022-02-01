from utils import get_puzzle_input


def count_depth_increase(data: list[int]) -> int:
    count = 0
    last, *data = data
    for depth in data:
        if depth > last:
            count += 1
        last = depth

    return count


if __name__ == "__main__":
    if puzzle_input := get_puzzle_input("day1.input", return_type=int):
        print(count_depth_increase(puzzle_input))
