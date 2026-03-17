import time

def print_board(board, n):
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                print("Q ", end="") 
            else:
                print(". ", end="") 
        print()
    print("-" * (n * 2))

def is_safe(board, row, col, n):
    # Cek baris yang sama di  kiri
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Cek diagonal atas kiri
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Cek diagonal bawah kiri
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    if col >= n:
        return True 

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1 
            
            print(f"-> Mencoba meletakkan Ratu di baris {i}, kolom {col}:")
            print_board(board, n)
            time.sleep(0) 
            if solve_n_queens_util(board, col + 1, n):
                return True 
            print(f"<- BACKTRACK! Menghapus Ratu dari baris {i}, kolom {col}")
            board[i][col] = 0
            print_board(board, n)
            time.sleep(0)
    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solusi tidak ditemukan.")
        return False

    print("SOLUSI:")
    print_board(board, n)
    return True

if __name__ == "__main__":
    solve_n_queens(4)