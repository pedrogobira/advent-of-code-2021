from utils import get_puzzle_input


def count_depth_increase(data: list) -> int:
    count = 0
    first_group = data[:3]
    data = data[3:]
    second_group = []

    for i, _ in enumerate(data):
        second_group.append(first_group[1])
        second_group.append(first_group[2])
        second_group.append(data[i])
        if sum(second_group) > sum(first_group):
            count += 1

        first_group = second_group
        second_group = []

    return count


if __name__ == "__main__":
    if puzzle_input := get_puzzle_input("day1.input", return_type=int):
        print(count_depth_increase(puzzle_input))
