from utils import get_puzzle_input


def parse_data(data: list[str]) -> tuple:
    patterns = list(
        filter(
            None, map(lambda line: line.strip().split("|")[0].strip().split(" "), data)
        )
    )
    outputs = list(
        filter(
            None, map(lambda line: line.strip().split("|")[1].strip().split(" "), data)
        )
    )

    return (patterns, outputs)


def sum_output_values(data: tuple) -> int:
    patterns, outputs = data
    processed_outputs = []

    target = len(outputs) - 1
    index = 0

    while index <= target:
        groups = {number: [] for number in range(2, 8)}
        for digit in patterns[index]:
            size = len(digit)
            groups[size].append(digit)

        one = sorted(groups[2][0])
        four = sorted(groups[4][0])
        seven = sorted(groups[3][0])
        eight = sorted(groups[7][0])

        top_segment = [char for char in seven if char not in one][0]
        bottom_or_bottom_left = [
            char for char in eight if char not in four and char not in seven
        ]
        # no assumption
        first_segment, second_segment = bottom_or_bottom_left

        nine = []
        for digit in groups[6]:
            digit = sorted(digit)
            if not (first_segment in digit and second_segment in digit):
                nine = digit

        bottom_segment = [
            char for char in nine if char not in four and char not in top_segment
        ][0]
        bottom_left_segment = (
            first_segment if second_segment in bottom_segment else second_segment
        )

        two = []
        for digit in groups[5]:
            digit = sorted(digit)
            if bottom_left_segment in digit:
                two = digit

        top_left_segment = [
            char for char in eight if char not in two and char not in one
        ][0]
        middle_segment = [
            char
            for char in eight
            if char
            not in [
                *top_segment,
                *top_left_segment,
                bottom_left_segment,
                *bottom_segment,
                *one,
            ]
        ][0]

        five = []
        three = []
        for digit in groups[5]:
            digit = sorted(digit)
            if top_left_segment in digit:
                five = digit
            elif bottom_left_segment not in digit:
                three = digit

        top_right_segment = [
            char for char in eight if char not in five and char != bottom_left_segment
        ][0]

        zero = []
        six = []
        for digit in groups[6]:
            digit = sorted(digit)
            if middle_segment not in digit:
                zero = digit
            elif top_right_segment not in digit:
                six = digit

        numeric_output = []

        for output in outputs[index]:
            output = sorted(output)
            if output == zero:
                numeric_output.append("0")
            elif output == one:
                numeric_output.append("1")
            elif output == two:
                numeric_output.append("2")
            elif output == three:
                numeric_output.append("3")
            elif output == four:
                numeric_output.append("4")
            elif output == five:
                numeric_output.append("5")
            elif output == six:
                numeric_output.append("6")
            elif output == seven:
                numeric_output.append("7")
            elif output == eight:
                numeric_output.append("8")
            elif output == nine:
                numeric_output.append("9")

        numeric_output = int("".join(numeric_output))
        processed_outputs.append(numeric_output)

        index += 1

    return sum(processed_outputs)


if __name__ == "__main__":
    if puzzle_input := get_puzzle_input("day8.input"):
        clean_data = parse_data(puzzle_input)
        count_result = sum_output_values(clean_data)
        print(count_result)
