def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


def main():
    n = 4
    solutions = solve_n_queens(n)
    print(f"Number of solutions for {n}-queens: {len(solutions)}")
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
