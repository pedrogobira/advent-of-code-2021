from utils import get_puzzle_input


def get_position(movements: list[str]) -> tuple[int, int]:
    horizontal = depth = 0
    for movement in movements:
        match movement.split():
            case ["forward", parameter]:
                horizontal += int(parameter)
            case ["up", parameter]:
                depth -= int(parameter)
            case ["down", parameter]:
                depth += int(parameter)

    return (horizontal, depth)


if __name__ == "__main__":
    if puzzle_input := get_puzzle_input("day2.input"):
        position = get_position(puzzle_input)
        print(
            f"The multiplication of the horizontal position by the depth is equal to {position[0] * position[1]}"
        )
