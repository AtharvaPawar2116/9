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














































































































































































def solve_n_queens_bnb(n):
    # Inner recursive function using backtracking and branch & bound
    def solve(col, board, left_row, lower_diag, upper_diag, solutions):
        if col == n:  # All columns filled => a solution is found
            solutions.append(["".join(row) for row in board])  # Save board config
            return
        
        for row in range(n):  # Try placing queen in all rows of current column
            # Check if placing at (row, col) is safe using branch and bound
            if left_row[row] == 0 and lower_diag[row + col] == 0 and upper_diag[n - 1 + col - row] == 0:
                board[row][col] = 'Q'                  # Place queen
                left_row[row] = 1                      # Mark row as used
                lower_diag[row + col] = 1              # Mark '\' diagonal
                upper_diag[n - 1 + col - row] = 1      # Mark '/' diagonal

                solve(col + 1, board, left_row, lower_diag, upper_diag, solutions)  # Recurse to next column

                # Backtrack if placing queen doesn't lead to solution
                board[row][col] = '.'
                left_row[row] = 0
                lower_diag[row + col] = 0
                upper_diag[n - 1 + col - row] = 0

    # Initialization
    board = [['.' for _ in range(n)] for _ in range(n)]  # Create n x n board with '.'
    left_row = [0] * n                     # Row constraint array
    lower_diag = [0] * (2 * n - 1)         # '\' diagonal (r + c)
    upper_diag = [0] * (2 * n - 1)         # '/' diagonal (n - 1 + c - r)
    solutions = []                         # Stores all valid solutions

    solve(0, board, left_row, lower_diag, upper_diag, solutions)  # Start recursion from column 0

    # Print results
    print(f"\nTotal solutions for {n}-Queens: {len(solutions)}")
    for i, sol in enumerate(solutions, start=1):
        print(f"\nSolution {i}:")
        for row in sol:
            print(row)

# Run the function with user input
n = int(input("Enter the number of queens: "))
solve_n_queens_bnb(n)
