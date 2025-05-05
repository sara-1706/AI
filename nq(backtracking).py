def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, n):
    if row == n:
        return True  # All queens are placed successfully
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place queen in the current position
            if solve_nqueens(board, row + 1, n):
                return True  # Proceed to the next row
            board[row] = -1  # Backtrack if no solution found
    
    return False  # If no solution is found in this row

def print_solution(board, n):
    for i in range(n):
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(" ".join(row))

def nqueens_backtracking(n):
    board = [-1] * n  # Initialize board with -1 (no queens placed)
    
    if solve_nqueens(board, 0, n):
        print_solution(board, n)
    else:
        print("Solution does not exist.")

# Get user input for n
n = int(input("Enter the number of queens (n): "))
nqueens_backtracking(n)

