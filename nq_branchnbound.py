def is_safe_with_bound(row, col, cols, diag1, diag2):
    # Check if the column or diagonal is under attack
    return not (cols[col] or diag1[row - col] or diag2[row + col])

def place_queen(board, row, col, cols, diag1, diag2):
    board[row] = col
    cols[col] = True
    diag1[row - col] = True
    diag2[row + col] = True

def remove_queen(row, col, cols, diag1, diag2):
    cols[col] = False
    diag1[row - col] = False
    diag2[row + col] = False

def solve_nqueens_bound(board, row, n, cols, diag1, diag2):
    if row == n:
        return True  # All queens are placed successfully
    
    for col in range(n):
        if is_safe_with_bound(row, col, cols, diag1, diag2):
            place_queen(board, row, col, cols, diag1, diag2)
            if solve_nqueens_bound(board, row + 1, n, cols, diag1, diag2):
                return True
            remove_queen(row, col, cols, diag1, diag2)  # Backtrack
    
    return False  # No solution found in this branch

def print_solution(board, n):
    for i in range(n):
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(" ".join(row))

def nqueens_branch_and_bound(n):
    board = [-1] * n
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)  # Track diagonals (r - c) range [-n+1, n-1]
    diag2 = [False] * (2 * n - 1)  # Track diagonals (r + c) range [0, 2n-2]
    
    if solve_nqueens_bound(board, 0, n, cols, diag1, diag2):
        print_solution(board, n)
    else:
        print("Solution does not exist.")

# Get user input for n
n = int(input("Enter the number of queens (n): "))
nqueens_branch_and_bound(n)

