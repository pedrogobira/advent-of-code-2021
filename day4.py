from utils import get_puzzle_input


class Board:
    def __init__(self, data: list[dict]) -> None:
        self.data = data
        self._marked_positions = []

    def mark_number(self, number: str) -> None:
        for line in self.data:
            if value := line.get(number):
                value["marked"] = 1
                self._marked_positions.append(value["position"])
                return None

    def is_winner(self) -> bool:
        columns_votes = {i: 0 for i in range(5)}

        for position in self._marked_positions:
            columns_votes[position] += 1
            if 5 in columns_votes.values():
                return True

        for line in self.data:
            if all(values["marked"] == 1 for values in line.values()):
                return True

        return False

    def unmarked_numbers_sum(self) -> int:
        sum = 0

        for line in self.data:
            for key, value in line.items():
                if value["marked"] != 1:
                    sum += int(key)

        return sum


class Bingo:
    def __init__(self, raw_data: list[str]) -> None:
        self.raw_data = raw_data
        self._boards: list[Board] = []
        self._drawn_numbers = []

    def _setup_bingo(self) -> None:
        lines = []
        board = None

        for line in self.raw_data:
            if line.find(",") != -1:
                self._drawn_numbers = line.split(",")
            elif line == "":
                lines = []
                board = Board(lines)
                self._boards.append(board)
            else:
                split_line = line.split(" ")
                split_line = list(filter(None, split_line))
                line = {
                    item: {"position": i, "marked": 0}
                    for i, item in enumerate(split_line)
                    if item != ""
                }
                lines.append(line)

    def _bingo(self) -> tuple[Board, str] | None:
        for number in self._drawn_numbers:
            for board in self._boards:
                board.mark_number(number)
                if board.is_winner():
                    return (board, number)

    def _calculate_score(self, result: tuple[Board, str] | None) -> int:
        if result is None:
            return -1

        board, drawn_number = result
        return board.unmarked_numbers_sum() * int(drawn_number)

    def start(self) -> int:
        self._setup_bingo()
        result = self._bingo()
        score = self._calculate_score(result)
        return score


if __name__ == "__main__":
    # test {{{
    # puzzle_input = [
    #     "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    #     "",
    #     "22 13 17 11 0",
    #     "8 2 23 4 24",
    #     "21 9 1 16 7",
    #     "6 10 3 18 5",
    #     "1 12 20 15 19",
    #     "",
    #     "3 15 0 2 22",
    #     "9 18 13 17 5",
    #     "19 8 7 25 23",
    #     "20 11 10 24 4",
    #     "14 21 16 12 6",
    #     "",
    #     "14 21 17 24 4",
    #     "10 16 15 9 19",
    #     "18 8 23 26 20",
    #     "22 11 13 6 5",
    #     "2 0 12 3 7",
    # ]
    #
    # bingo = Bingo(puzzle_input)
    # result = bingo.start()
    # print(result)
    # }}}

    # main{{{
    # the first line are the drawn numbers and blank lines mean the beginning/end of a board
    if puzzle_input := get_puzzle_input("day4.input"):
        bingo = Bingo(puzzle_input)
        result = bingo.start()
        print(result)
    # }}}
