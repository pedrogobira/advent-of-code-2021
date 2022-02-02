from utils import get_puzzle_input


# -- PLAN -- {{{
# STEPS
# 2 new binaries: gamma_rate, epsilon_rate
# gamma_rate: composed by the most common bits
# epsilon_rate: composed by the least common bits
# check power consumption: gamma_rate * epsilon_rate
#
# IDEAS
# size of one binary
# create dict based on that
#
# example for binaries with 5 bits:
# {
#     0: {
#             "0": int,
#             "1": int
#         },
#     1: {
#             "0": int,
#             "1": int
#         },
#     2: {
#             "0": int,
#             "1": int
#         },
#     3: {
#             "0": int,
#             "1": int
#         },
#     4: {
#             "0": int,
#             "1": int
#         }
# }
# }}}
def power_consumption(binaries: list[str]) -> int:
    votes = {}
    first, *binaries = binaries

    # populate votes dict based on the size of the binary number
    for i, _ in enumerate(first):
        votes[i] = {"0": 0, "1": 0}

    # conduct votes according with repeated bits in binaries
    for binary in binaries:
        for i, bit in enumerate(binary):
            if count := votes.get(i):
                if bit == "0":
                    count["0"] = count.get("0") + 1
                elif bit == "1":
                    count["1"] = count.get("1") + 1

    gamma_rate = epsilon_rate = ""

    # calculate gamma_rate and epsilon_rate based on votes
    for count in votes.values():
        if (zero := count.get("0")) and (one := count.get("1")):
            if zero > one:
                gamma_rate += "0"
                epsilon_rate += "1"
            else:
                gamma_rate += "1"
                epsilon_rate += "0"

    consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

    return consumption


if __name__ == "__main__":
    if puzzle_input := get_puzzle_input("day3.input"):
        print(power_consumption(puzzle_input))
