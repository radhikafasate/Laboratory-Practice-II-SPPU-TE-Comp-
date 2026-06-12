from queue import PriorityQueue

# Goal state of 8 puzzle
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Heuristic function: Misplaced tiles
def calculate_h(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] != goal[i][j]:
                count += 1
    return count


# Find position of empty tile (0)
def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j


# Print board
def print_board(board):
    for row in board:
        print(row)
    print()


# Check valid position
def is_safe(x, y):
    return 0 <= x < 3 and 0 <= y < 3


# A* Node class
class Node:
    def __init__(self, board, x, y, g, parent):
        self.board = board
        self.x = x
        self.y = y
        self.g = g                   # cost so far
        self.h = calculate_h(board)  # heuristic
        self.f = self.g + self.h     # total cost
        self.parent = parent

    # For priority queue comparison
    def __lt__(self, other):
        return self.f < other.f


# Print solution path
def print_path(node):
    if node is None:
        return
    print_path(node.parent)
    print_board(node.board)


# A* Search Algorithm
def a_star(start):
    pq = PriorityQueue()

    x, y = find_blank(start)
    root = Node(start, x, y, 0, None)

    pq.put(root)

    # Possible moves: up, down, left, right
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while not pq.empty():
        current = pq.get()

        # Goal check
        if current.h == 0:
            print("Solution Found:\n")
            print_path(current)
            return

        # Try all 4 moves
        for i in range(4):
            new_x = current.x + dx[i]
            new_y = current.y + dy[i]

            if is_safe(new_x, new_y):
                new_board = [row[:] for row in current.board]

                # swap blank
                new_board[current.x][current.y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[current.x][current.y]

                child_x, child_y = new_x, new_y

                child = Node(new_board, child_x, child_y, current.g + 1, current)

                pq.put(child)


# ---------------- MAIN ----------------
start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

a_star(start_state)