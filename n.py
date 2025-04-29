def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, left_row, upper_diagonal, lower_diagonal, N):
    return not left_row[row] and not lower_diagonal[row + col] and not upper_diagonal[N - 1 + col - row]

def solve_n_queens(col, board, left_row, upper_diagonal, lower_diagonal, N):
    if col == N:
        print("One of the solutions:")
        print_solution(board)
        return True  # Change to False if you want to print all solutions

    for row in range(N):
        if is_safe(board, row, col, left_row, upper_diagonal, lower_diagonal, N):
            board[row][col] = 1
            left_row[row] = lower_diagonal[row + col] = upper_diagonal[N - 1 + col - row] = True

            if solve_n_queens(col + 1, board, left_row, upper_diagonal, lower_diagonal, N):
                return True

            board[row][col] = 0
            left_row[row] = lower_diagonal[row + col] = upper_diagonal[N - 1 + col - row] = False

    return False

def n_queens_branch_and_bound():
    N = int(input("Enter the value of N (number of queens): "))
    board = [[0 for _ in range(N)] for _ in range(N)]
    left_row = [False] * N
    upper_diagonal = [False] * (2 * N - 1)
    lower_diagonal = [False] * (2 * N - 1)

    if not solve_n_queens(0, board, left_row, upper_diagonal, lower_diagonal, N):
        print("No solution exists.")

n_queens_branch_and_bound()
