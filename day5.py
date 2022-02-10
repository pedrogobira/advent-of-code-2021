from utils import get_puzzle_input
from collections import Counter


def parse_input(puzzle_input: list[str]) -> list[list[tuple]]:
    data = []

    for line in puzzle_input:
        line = line.split("->")
        coordinate_pair = []
        for item in line:
            coordinate = item.strip().split(",")
            coordinate_pair.append((int(coordinate[0]), int(coordinate[1])))
        data.append(coordinate_pair)

    return data


def count_overlaps(data: list[list[tuple]]) -> int:
    count = 0
    coordinates = []

    for coordinate in data:
        coordinate = sorted(coordinate)
        if coordinate[0][0] == coordinate[1][0] or coordinate[0][1] == coordinate[1][1]:
            horizontal_range = range(coordinate[0][0], coordinate[1][0] + 1)
            vertical_range = range(coordinate[0][1], coordinate[1][1] + 1)
            coordinates += [(x, y) for x in horizontal_range for y in vertical_range]

    counter = Counter(coordinates)
    count = sum(1 for value in counter.values() if value > 1)

    return count


if __name__ == "__main__":
    # test {{{
    # puzzle_input = [
    #     "0,9 -> 5,9",
    #     "8,0 -> 0,8",
    #     "9,4 -> 3,4",
    #     "2,2 -> 2,1",
    #     "7,0 -> 7,4",
    #     "6,4 -> 2,0",
    #     "0,9 -> 2,9",
    #     "3,4 -> 1,4",
    #     "0,0 -> 8,8",
    #     "5,5 -> 8,2",
    # ]
    #
    # data = parse_input(puzzle_input)
    # print(count_overlaps(data))
    # }}}

    # main {{{
    if puzzle_input := get_puzzle_input("day5.input"):
        data = parse_input(puzzle_input)
        print(count_overlaps(data))
    # }}}
