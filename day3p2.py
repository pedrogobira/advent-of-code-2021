from utils import get_puzzle_input


# --- PLAN --- {{{
# STEPS
# find life_support_rating: oxygen_generator_rating * co2_scrubber_rating
# consider just one bit of a binary number per time
# bit criteria: oxygen = most common (preference 1); co2 = least common (preference 0)
# one number left = result; otherwise, repeat the process using the next bit
# }}}
def oxygen_generator_rating(binaries: list[str]) -> int:
    binary_size = len(binaries[0])

    for i in range(binary_size):
        zero = one = 0

        for binary in binaries:
            if binary[i] == "0":
                zero += 1
            elif binary[i] == "1":
                one += 1

        if len(binaries) > 1:
            if one >= zero:
                binaries = [binary for binary in binaries if binary[i] == "1"]
            else:
                binaries = [binary for binary in binaries if binary[i] == "0"]

    rating = int(binaries.pop(), 2)

    return rating


def co2_scrubber_rating(binaries: list[str]) -> int:
    binary_size = len(binaries[0])

    for i in range(binary_size):
        zero = one = 0

        for binary in binaries:
            if binary[i] == "0":
                zero += 1
            elif binary[i] == "1":
                one += 1

        if len(binaries) > 1:
            if one >= zero:
                binaries = [binary for binary in binaries if binary[i] == "0"]
            else:
                binaries = [binary for binary in binaries if binary[i] == "1"]

    rating = int(binaries.pop(), 2)

    return rating


if __name__ == "__main__":
    if puzzle_input := get_puzzle_input("day3.input"):
        life_support_rating = oxygen_generator_rating(
            puzzle_input
        ) * co2_scrubber_rating(puzzle_input)
        print(life_support_rating)
