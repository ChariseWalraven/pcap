# Your task is to write a program which:
# reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
# outputs Yes if the Sudoku is valid, and No otherwise.


# - each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
# - each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
# - each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

def get_cols_from_board(board: list) -> list:
    cols_as_rows = []
    for i in range(len(board)):
        col = []
        for row in board:
            col.append(row[i])
        cols_as_rows.append(col)
    return cols_as_rows


def get_subsquares_from_board(board: list) -> bool:
    subsquares_as_rows = []
    for row_start in range(0, 9, 3):
        for col_start in range(0, 9, 3):
            subsquare = []
            for j in range(3):
                for k in range(3):
                    subsquare.append(board[j + row_start][k + col_start])
            subsquares_as_rows.append(subsquare)

    return subsquares_as_rows


def are_all_rows_valid(rows: list) -> bool:
    num_rows_with_all_9_digits = 0
    for row in rows:
        digits_in_row = []
        for digit in row:
            if digit not in digits_in_row:
                digits_in_row.append(digit)
        if len(digits_in_row) == 9:
            num_rows_with_all_9_digits += 1
    return num_rows_with_all_9_digits == 9


def are_all_columns_valid(board: list) -> bool:
    cols_as_rows = get_cols_from_board(board)
    return are_all_rows_valid(cols_as_rows)


def are_subsquares_valid(board: list) -> bool:
    subsquares_as_rows = get_subsquares_from_board(board)
    return are_all_rows_valid(subsquares_as_rows)


def get_user_input():
    board = []
    for i in range(9):
        row_str = input(f'Please enter the digits of row {i + 1}: ')
        row = [int(c) for c in row_str.replace(' ', '')]
        board.append(row)
    return board


def program():
    print('=' * 39, 'Sudoku Checker', '=' * 39)
    print('Checks if the digits in a sudoku board are valid.')
    print('Please note that the program only accepts digits; any other characters will cause it to fail.', end='\n\n')
    board = get_user_input()
    rows_valid = are_all_rows_valid(board)
    cols_valid = are_all_columns_valid(board)
    subsquares_valid = are_subsquares_valid(board)

    if rows_valid and cols_valid and subsquares_valid:
        print('Yes')
    else:
        print('No')

# Test Data

# valid_board = [
#     [2, 9, 5, 7, 4, 3, 8, 6, 1],
#     [4, 3, 1, 8, 6, 5, 9, 2, 7],
#     [8, 7, 6, 1, 9, 2, 5, 4, 3],
#     [3, 8, 7, 4, 5, 9, 2, 1, 6],
#     [6, 1, 2, 3, 8, 7, 4, 9, 5],
#     [5, 4, 9, 2, 1, 6, 7, 3, 8],
#     [7, 6, 3, 5, 2, 4, 1, 8, 9],
#     [9, 2, 8, 6, 7, 1, 3, 5, 4],
#     [1, 5, 4, 9, 3, 8, 6, 7, 2]
# ]


invalid_subsquares_board = [
    [1, 9, 5, 7, 4, 3, 8, 6, 2],
    [4, 3, 1, 8, 6, 5, 9, 2, 7],
    [8, 7, 6, 1, 9, 2, 5, 4, 3],
    [3, 8, 7, 4, 5, 9, 2, 1, 6],
    [6, 1, 2, 3, 8, 7, 4, 9, 5],
    [5, 4, 9, 2, 1, 6, 7, 3, 8],
    [7, 6, 3, 5, 2, 4, 1, 8, 9],
    [9, 2, 8, 6, 7, 1, 3, 5, 4],
    [2, 5, 4, 9, 3, 8, 6, 7, 1]
]

# 295743861
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 154938672
# Yes

# 195 743 862
# 431 865 927
# 876 192 543

# 387 459 216
# 612 387 495
# 549 216 738

# 763 524 189
# 928 671 354
# 254 938 671
# No


# print(are_all_rows_valid(invalid_subsquares_board))
# print(are_all_columns_valid(invalid_subsquares_board))
# print(are_subsquares_valid(invalid_subsquares_board))


if __name__ == '__main__':
    try:
        program()
    except (ValueError, TypeError):
        print('Whoops, something went wrong when processing the data. Are you sure you entered the correct data?')
    except Exception as e:
        print('Whoops, something went wrong!', e)
