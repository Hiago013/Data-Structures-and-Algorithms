def is_safe(board, row, col):
    # Check if no queen is present in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def backtrack_n_queens(x, row, n):
        if row == n:
            solutions.append(x[:])  # Found a solution
        else:
            for col in range(n):
                if is_safe(x, row, col):
                    x[row] = col
                    backtrack_n_queens(x, row + 1, n)

    backtrack_n_queens(board, 0, n)
    return solutions

# Example usage:
n = 4  # Change this to the desired board size
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens: {len(solutions)}")
print("Solutions:")
for sol in solutions:
    print(sol)
