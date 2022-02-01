from utils import get_puzzle_input


def get_position(movements: list[str]) -> tuple[int, int]:
    horizontal = depth = aim = 0
    for movement in movements:
        match movement.split():
            case ["up", parameter]:
                aim -= int(parameter)
            case ["down", parameter]:
                aim += int(parameter)
            case ["forward", parameter]:
                parameter = int(parameter)
                horizontal += parameter
                depth += parameter * aim

    return (horizontal, depth)


if __name__ == "__main__":
    if puzzle_input := get_puzzle_input("day2.input"):
        position = get_position(puzzle_input)
        print(
            f"The multiplication of the horizontal position by the depth is equal to {position[0] * position[1]}"
        )
