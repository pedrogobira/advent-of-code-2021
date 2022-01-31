def get_data() -> list | None:
    data = []
    try:
        with open("day1.input", "r") as file:
            for line in file:
                data.append(int(line.rstrip("\n")))
    except IOError:
        print("input not found")

    return data


def count_depth_increase(data: list) -> int:
    count = 0
    last, *data = data
    for depth in data:
        if depth > last:
            count += 1
        last = depth

    return count


if __name__ == "__main__":
    if puzzle_input := get_data():
        print(count_depth_increase(puzzle_input))

