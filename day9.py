from utils import get_puzzle_input


if __name__ == "__main__":
    matrix = get_puzzle_input("day9.input")

    row_len = len(matrix)
    column_len = len(matrix[0])

    low_points = []
    dont_check = []

    for row_index, row in enumerate(matrix):
        for column_index, number in enumerate(row):
            int_number = int(number)
            candidate_score = 0

            if row_index - 1 < 0:
                dont_check.append("top")
            if column_index + 1 > column_len - 1:
                dont_check.append("right")
            if row_index + 1 > row_len - 1:
                dont_check.append("bottom")
            if column_index - 1 < 0:
                dont_check.append("left")

            if not "top" in dont_check:
                if int_number < int(matrix[row_index - 1][column_index]):
                    candidate_score += 1
            if not "right" in dont_check:
                if int_number < int(row[column_index + 1]):
                    candidate_score += 1
            if not "bottom" in dont_check:
                if int_number < int(matrix[row_index + 1][column_index]):
                    candidate_score += 1
            if not "left" in dont_check:
                if int_number < int(row[column_index - 1]):
                    candidate_score += 1

            if len(dont_check) + candidate_score == 4:
                low_points.append(int_number)

            dont_check.clear()

    low_points_sum = 0

    for point in low_points:
        low_points_sum += point + 1

    print(low_points_sum)
