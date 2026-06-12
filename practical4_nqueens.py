count = 0

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


def is_safe_backtracking(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_backtracking(board, row, n):
    global count
    if row == n:
        count += 1
        print("Solution", count)
        print_board(board, n)
        return
    
    for col in range(n):
        if is_safe_backtracking(board, row, col, n):
            board[row][col] = 1
            solve_backtracking(board, row + 1, n)
            board[row][col] = 0



def solve_branch_bound(board, row, n, cols, d1, d2):
    global count
    if row == n:
        count += 1
        print("Solution", count)
        print_board(board, n)
        return

    for col in range(n):
        if col in cols:
            continue
        if (row - col) in d1:
            continue
        if (row + col) in d2:
            continue
        board[row][col] = 1
        cols.add(col)
        d1.add(row - col)
        d2.add(row + col)

        solve_branch_bound(board, row + 1, n, cols, d1, d2)

        board[row][col] = 0
        cols.remove(col)
        d1.remove(row - col)
        d2.remove(row + col)


while True:
    print("\n==========================")
    print("      N-QUEENS MENU")
    print("==========================")
    print("1. Solve using Backtracking")
    print("2. Solve using Branch and Bound")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        n = int(input("Enter N: "))
        count = 0

        # Create empty matrix
        board = [[0 for _ in range(n)] for _ in range(n)]

        print("\nSolutions using Backtracking:\n")
        solve_backtracking(board, 0, n)

        print("Total solutions:", count)

    elif choice == '2':
        n = int(input("Enter N: "))
        count = 0
       
        board = [[0 for _ in range(n)] for _ in range(n)]

        cols = set()
        d1 = set()  
        d2 = set()  

        print("\nSolutions using Branch and Bound:\n")
        solve_branch_bound(board, 0, n, cols, d1, d2)

        print("Total solutions:", count)

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")